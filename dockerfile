FROM nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04
ARG USER
ARG PASSWD
RUN apt-get update && apt-get install -y sudo git htop wget libncurses5-dev curl
RUN useradd -m $USER && echo "$USER:$USER" | chpasswd && adduser --disabled-password --gecos '' $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER $USER
RUN printf "$PASSWD\n$PASSWD\n" | sudo passwd $USER
WORKDIR /home/$USER

ENV HOME /home/$USER

#install minoconda

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $HOME/miniconda3 && \
    rm ~/miniconda.sh

#install vim
RUN mkdir -p Application && \
        git clone https://github.com/vim/vim.git Application/vim && \
        cd Application/vim/src && \
        make && sudo make install && sudo cp vim /usr/bin

RUN git clone https://github.com/pjh4993/vim.git .vim && \
        cd .vim && git submodule init && git submodule update --recursive && \
        ln -s ~/.vim/.vimrc ~/.vimrc

RUN curl -sL https://deb.nodesource.com/setup_15.x | sudo -E bash - && \
        sudo apt-get install -y nodejs

# make non-activate conda commands available

ENV PATH=$HOME/.local/bin:$HOME/miniconda3/bin:$PATH
RUN echo ". $HOME/miniconda3/etc/profile.d/conda.sh" >> ~/.profile
RUN ["/bin/bash", "-c", "source $HOME/miniconda3/bin/activate root"]
RUN conda install python=3.9.1 -y
RUN conda update --name base --channel defaults conda -y
RUN conda install -c=conda-forge pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch -y
WORKDIR /home/$USER
RUN pip install opencv-python
CMD /bin/bash
