from ipykernel.kernelapp import IPKernelApp
from .kernel import BashKernel

kernel_classes = { "bash" : BashKernel,
                   "ghci" : BashKernel }

import argparse
parser = argparse.ArgumentParser(description='Launch a pexpect Jupyter kernel.')
parser.add_argument('repl_name',
                    help='Name of underlying REPL language, one of %s' % (l for l in kernel_classes))
parser.add_argument('-f', dest='filename')

args = parser.parse_args()
IPKernelApp.launch_instance(kernel_class=kernel_classes[args.repl_name])
