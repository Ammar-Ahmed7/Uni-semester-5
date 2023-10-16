#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <string.h>

#define PERM (O_RDWR | O_CREAT)

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input_file> <output_file>\n", argv[0]);
        return 1;
    }

    pid_t cat_pid, grep_pid;
    int pipe_fd[2];

    if (pipe(pipe_fd) == -1) {
        perror("Unable to create pipe");
        return 1;
    }

    cat_pid = fork();
    if (cat_pid == -1) {
        perror("Unable to create cat process");
        return 1;
    }

    if (cat_pid == 0) {
        close(pipe_fd[0]);

        dup2(pipe_fd[1], STDOUT_FILENO);
        close(pipe_fd[1]);

        execl("/bin/cat", "cat", argv[1], NULL);
    } else {
        close(pipe_fd[1]);

        grep_pid = fork();
        if (grep_pid == -1) {
            perror("Unable to create grep process");
            return 1;
        }

        if (grep_pid == 0) {
            int output_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0666);
            if (output_fd == -1) {
                perror("Unable to open output file");
                return 1;
            }

            dup2(pipe_fd[0], STDIN_FILENO);
            close(pipe_fd[0]);

            dup2(output_fd, STDOUT_FILENO);
            close(output_fd);

            execl("/bin/grep", "grep", "x", NULL);
        } else {
            close(pipe_fd[0]);

            int status;
            waitpid(cat_pid, &status, 0);
            waitpid(grep_pid, &status, 0);
        }
    }

    return 0;
}

