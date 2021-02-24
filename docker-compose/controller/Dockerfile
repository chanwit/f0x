FROM python:3.7
RUN pip install kopf

COPY controller.py /src/
CMD kopf run /src/controller.py --verbose
