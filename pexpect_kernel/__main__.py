from ipykernel.kernelapp import IPKernelApp
from .bash_kernel import BashKernel
from .ghci_kernel import GHCIKernel
from .kernel import set_filename

kernel_classes = { "bash" : BashKernel,
                   "ghci" : GHCIKernel }

import argparse
parser = argparse.ArgumentParser(description='Launch a pexpect Jupyter kernel.')
parser.add_argument('repl_name',
                    help='Name of underlying REPL language, one of %s' % (l for l in kernel_classes))
parser.add_argument('-f', dest='filename')

args = parser.parse_args()
set_filename(args.filename)
IPKernelApp.launch_instance(kernel_class=kernel_classes[args.repl_name])
