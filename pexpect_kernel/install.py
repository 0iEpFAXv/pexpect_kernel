import json
import os
import sys
import argparse

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory

kernel_jsons = { "bash": {"argv":[sys.executable, "-m", "pexpect_kernel", "bash",
                                  "-f", "{connection_file}"],
                          "display_name":"Bash",
                          "language":"bash",
                          "codemirror_mode":"shell",
                          "env":{"PS1": "$"}
                         },
                 "ghci": {"argv":[sys.executable, "-m", "pexpect_kernel", "ghci",
                                  "-f", "{connection_file}"],
                          "display_name":"GHCI",
                          "language":"haskell",
                          "codemirror_mode":"shell",
                          "env":{"PS1": "$"}
                         }
               }

def install_my_kernel_spec(repl_name, user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755) # Starts off as 700, not user readable
        with open(os.path.join(td, 'kernel.json'), 'w') as f:
            json.dump(kernel_jsons[repl_name], f, sort_keys=True)
        # TODO: Copy resources once they're specified

        print('Installing IPython kernel spec')
        KernelSpecManager().install_kernel_spec(td, repl_name, user=user, replace=True, prefix=prefix)

def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False # assume not an admin on non-Unix platforms

def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Install KernelSpec for Pexpect Kernel'
    )
    parser.add_argument('repl_name',
                        help='Name of underlying REPL language, one of %s' % (l for l in kernel_jsons)) 
    prefix_locations = parser.add_mutually_exclusive_group()

    prefix_locations.add_argument(
        '--user',
        help='Install KernelSpec in user homedirectory',
        action='store_true'
    )
    prefix_locations.add_argument(
        '--sys-prefix',
        help='Install KernelSpec in sys.prefix. Useful in conda / virtualenv',
        action='store_true',
        dest='sys_prefix'
    )
    prefix_locations.add_argument(
        '--prefix',
        help='Install KernelSpec in this prefix',
        default=None
    )

    args = parser.parse_args(argv)

    user = False
    prefix = None
    if args.sys_prefix:
        prefix = sys.prefix
    elif args.prefix:
        prefix = args.prefix
    elif args.user or not _is_root():
        user = True

    install_my_kernel_spec(args.repl_name, user=user, prefix=prefix)

if __name__ == '__main__':
    main()
