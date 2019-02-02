FROM jupyter/scipy-notebook

######## Installing Bash Kernel ########

USER root

RUN mkdir /var/lib/apt/lists/partial && \
    mkdir /pexpect_kernel && \
    chown $NB_UID /pexpect_kernel && \
    chown -R $NB_UID /home/jovyan && \
    chmod -R o+X /home/jovyan

USER $NB_UID

COPY pexpect_kernel/ /pexpect_kernel/bash_kernel
COPY flit.ini /pexpect_kernel/

RUN cd /pexpect_kernel && \
    ls -al . && \
    pip install bash_kernel && \
    python3 -m bash_kernel.install

WORKDIR $HOME


