# start by pulling the python image
FROM python:3.9-slim-buster

WORKDIR /Newhacks2022

# copy the requirements file into the image
COPY . .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

# copy every content from the local file to the image
COPY . /app

RUN export FLASK_APP=server.py
CMD ["flask", "run" ]
