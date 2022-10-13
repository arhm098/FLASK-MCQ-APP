# start by pulling the python image
FROM python:3.10


# copy the requirements file into the image
COPY /requirements.txt /requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

COPY . .

# switch working directory
WORKDIR /venv

RUN ls

# copy every content from the local file to the image

EXPOSE 5000

CMD ["python","app.py"]