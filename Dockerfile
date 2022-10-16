FROM python:3.7-alpine

# RUN apt-get -y install python3-pip
# # copy the requirements file into the image

COPY /requirements.txt /requirements.txt

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

COPY . .

# switch working directory
WORKDIR /venv


# copy every content from the local file to the image

EXPOSE 5000

CMD ["python","app.py"]