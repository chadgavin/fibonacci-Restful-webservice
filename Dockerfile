FROM python:3
ADD requirements.txt /
ADD calculate.py /
ADD main.py /
RUN apt-get update
RUN pip install -r requirements.txt
CMD python3 main.py
