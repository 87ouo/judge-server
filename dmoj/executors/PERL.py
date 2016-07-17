from .base_executor import ScriptExecutor


class Executor(ScriptExecutor):
    ext = '.pl'
    name = 'PERL'
    command = 'perl'
    command_paths = ['perl']
    test_program = 'print<>'
    syscalls = ['umtx_op']

    def get_cmdline(self):
        return ['perl', '-Mre=eval', self._code]
