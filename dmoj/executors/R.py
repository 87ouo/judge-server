from .base_executor import ScriptExecutor


class Executor(ScriptExecutor):
    ext = '.R'
    name = 'R'
    nproc = -1  # needs a bunch
    command = 'Rscript'
    test_program = 'writeLines(readLines(file("stdin")))'
    syscalls = ['mkdir', 'setup', 'fork', 'waitpid', 'wait4', 'getpgrp', 'execve']

    fs = ['/etc/passwd$', '/etc/nsswitch.conf$', '/etc/group$']

    def get_cmdline(self):
        return [self.get_command(), '--vanilla', self._code]
