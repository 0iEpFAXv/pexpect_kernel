from subprocess import check_output
from pexpect import replwrap
import pexpect
import os.path
import re

from .kernel import IREPLWrapper, Kernel, __version__

class BashKernel(Kernel):
    implementation = 'bash_kernel'
    implementation_version = __version__

    @property
    def banner(self):
        if self._banner is None:
            self._banner = check_output(['bash', '--version']).decode('utf-8')
        return self._banner

    language_info = {'name': 'bash',
                     'codemirror_mode': 'shell',
                     'mimetype': 'text/x-sh',
                     'file_extension': '.sh'}

    def create_wrapper(self):
        # Note: the next few lines mirror functionality in the
        # bash() function of pexpect/replwrap.py.  Look at the
        # source code there for comments and context for
        # understanding the code here.
        bashrc = os.path.join(os.path.dirname(pexpect.__file__), 'bashrc.sh')
        child = pexpect.spawn("bash", ['--rcfile', bashrc], echo=False,
                              encoding='utf-8', codec_errors='replace')
        ps1 = replwrap.PEXPECT_PROMPT[:5] + u'\[\]' + replwrap.PEXPECT_PROMPT[5:]
        ps2 = replwrap.PEXPECT_CONTINUATION_PROMPT[:5] + u'\[\]' + replwrap.PEXPECT_CONTINUATION_PROMPT[5:]
        prompt_change = u"PS1='{0}' PS2='{1}' PROMPT_COMMAND=''".format(ps1, ps2)

        # Using IREPLWrapper to get incremental output
        self.wrapper = IREPLWrapper(child, u'\$', prompt_change,
                                    extra_init_cmd="export PAGER=cat",
                                    line_output_callback=self.process_output)

    def do_complete(self, code, cursor_pos):
        code = code[:cursor_pos]
        default = {'matches': [], 'cursor_start': 0,
                   'cursor_end': cursor_pos, 'metadata': dict(),
                   'status': 'ok'}

        if not code or code[-1] == ' ':
            return default

        tokens = code.replace(';', ' ').split()
        if not tokens:
            return default

        matches = []
        token = tokens[-1]
        start = cursor_pos - len(token)

        if token[0] == '$':
            # complete variables
            cmd = 'compgen -A arrayvar -A export -A variable %s' % token[1:] # strip leading $
            output = self.wrapper.run_command(cmd).rstrip()
            completions = set(output.split())
            # append matches including leading $
            matches.extend(['$'+c for c in completions])
        else:
            # complete functions and builtins
            cmd = 'compgen -cdfa %s' % token
            output = self.wrapper.run_command(cmd).rstrip()
            matches.extend(output.split())

        if not matches:
            return default
        matches = [m for m in matches if m.startswith(token)]

        return {'matches': sorted(matches), 'cursor_start': start,
                'cursor_end': cursor_pos, 'metadata': dict(),
                'status': 'ok'}
