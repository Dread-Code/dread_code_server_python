FROM python:3.10-alpine3.16

# set the working directory
WORKDIR /dreadcode_api

# install dependencies
COPY requirements.txt .

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# copy the src to the folder
COPY . .

EXPOSE 8000

# start the server
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

