from subprocess import check_output
from pexpect import replwrap
import pexpect
import os.path
import re

from .kernel import IREPLWrapper, Kernel, __version__, get_filename

class GHCIKernel(Kernel):
    implementation = 'ghci_kernel'
    implementation_version = __version__

    @property
    def banner(self):
        if self._banner is None:
            self._banner = check_output(['bash', '--version']).decode('utf-8')
        return self._banner

    language_info = {'name': 'ghci',
                     'codemirror_mode': 'haskell',
                     'mimetype': 'text/x-haskell',
                     'file_extension': '.lhs'}

    def create_wrapper(self):
        #ghci_path = os.path.abspath(os.path.dirname(get_filename()))
        
        child = pexpect.spawn("stack", ['ghci'], echo=False,
                              encoding='utf-8', codec_errors='replace')
        prompt_change = u':set prompt "{0}"'
        extra_init_cmd = u':set prompt-cont "{0}"'.format(replwrap.PEXPECT_CONTINUATION_PROMPT)

        # Using IREPLWrapper to get incremental output
        self.wrapper = IREPLWrapper(child, u'\n.*> ', prompt_change,
                                    extra_init_cmd=extra_init_cmd,
                                    line_output_callback=self.process_output)
        print("Finished setting up IREPLWrapper!")

    # See https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/ghci.html#ghci-commands for :complete
#     def do_complete(self, code, cursor_pos):
#         code = code[:cursor_pos]
#         default = {'matches': [], 'cursor_start': 0,
#                    'cursor_end': cursor_pos, 'metadata': dict(),
#                    'status': 'ok'}

#         if not code or code[-1] == ' ':
#             return default

#         tokens = code.replace(';', ' ').split()
#         if not tokens:
#             return default

#         matches = []
#         token = tokens[-1]
#         start = cursor_pos - len(token)

#         if token[0] == '$':
#             # complete variables
#             cmd = 'compgen -A arrayvar -A export -A variable %s' % token[1:] # strip leading $
#             output = self.wrapper.run_command(cmd).rstrip()
#             completions = set(output.split())
#             # append matches including leading $
#             matches.extend(['$'+c for c in completions])
#         else:
#             # complete functions and builtins
#             cmd = 'compgen -cdfa %s' % token
#             output = self.wrapper.run_command(cmd).rstrip()
#             matches.extend(output.split())

#         if not matches:
#             return default
#         matches = [m for m in matches if m.startswith(token)]

#         return {'matches': sorted(matches), 'cursor_start': start,
#                 'cursor_end': cursor_pos, 'metadata': dict(),
#                 'status': 'ok'}
