FROM python:3.8

RUN pip install virtualenv

# TODO: check repo URL and visibility
RUN git clone https://github.com/biabs1/Treefix.git
RUN cd Treefix

RUN virtualenv treefix_env
RUN source treefix_env/bin/activate

RUN pip install -r requirements.txt
RUN pip install -e ./

CMD ["/bin/bash"]