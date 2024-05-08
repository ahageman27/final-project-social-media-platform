FROM python:3.12

ADD src /src
WORKDIR /src

# add and install requirements
ADD requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP=/src/__init__.py
ENV PYTHONPATH="${PYTHONPATH}:/src"

# flask run
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
