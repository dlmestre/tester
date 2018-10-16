FROM python:2.7

COPY ./dev_tester.py /dev_tester.py
COPY ./Jenkinsfile /Jenkinsfile

CMD ["python","./dev_tester.py"]