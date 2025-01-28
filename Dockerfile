FROM python:3.8

RUN pip install virtualenv

ENV PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/venv \
    PATH="/venv/bin:$PATH"

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip

RUN git clone https://github.com/sola-st/Treefix.git

WORKDIR /Treefix
  
RUN pip install -r requirements.txt
RUN pip install -e ./

CMD ["bash"]