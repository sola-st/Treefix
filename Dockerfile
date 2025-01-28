FROM python:3.8

RUN pip install virtualenv

RUN git clone https://github.com/sola-st/Treefix.git
WORKDIR Treefix

RUN virtualenv treefix_env
RUN bash -c "source treefix_env/bin/activate"

RUN pip install -r requirements.txt
RUN pip install -e ./

CMD ["/bin/bash"]