A Jupyter kernel based on pexpect
=================================

This requires IPython 3.

Docker Usage
------------

For docker based usage, set up these environment variables.  These values are just examples, but the directories should allow reading and writing.  The JOVYAN_STACK_PATH is used by ghci_jupyter_lab container.

.. code:: shell
    
    export JUPYTER_WORKSPACE=/home/someuser/code
    export JOVYAN_STACK_PATH=/home/someuser/jovyan.stack

Then execute the one of the following scripts:

    ./bash_jupyter_lab.sh
    
OR 

    ./ghci_jupyter_lab.sh   
   

Manual Usage
------------

For manual installation or global usage:

To install:

.. code:: shell

    pip install pexpect_kernel
    python -m pexpect_kernel.install bash

To use it, run one of:

.. code:: shell

    jupyter notebook
    # In the notebook interface, select Bash from the 'New' menu
    jupyter qtconsole --kernel bash
    jupyter console --kernel bash

Further Documentation
---------------------

For details of how this works, see the Jupyter docs on `wrapper kernels
<http://jupyter-client.readthedocs.org/en/latest/wrapperkernels.html>`_, and
Pexpect's docs on the `replwrap module
<http://pexpect.readthedocs.org/en/latest/api/replwrap.html>`_
