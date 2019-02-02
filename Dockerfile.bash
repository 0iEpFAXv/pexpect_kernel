FROM jupyter/scipy-notebook

######## Installing Bash Kernel ########

USER root

RUN mkdir /var/lib/apt/lists/partial && \
    mkdir /pexpect_kernel && \
    chown $NB_UID /pexpect_kernel && \
    chown -R $NB_UID /home/jovyan && \
    chmod -R o+X /home/jovyan

USER $NB_UID

COPY pexpect_kernel/ /pexpect_kernel/pexpect_kernel
COPY setup.py /pexpect_kernel/

RUN cd /pexpect_kernel && \
    pip install /pexpect_kernel && \
    python3 -m pexpect_kernel.install bash

WORKDIR $HOME


