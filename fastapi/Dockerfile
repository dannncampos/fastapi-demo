FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir /fastapi

# Bundle app source
COPY requirements.txt /fastapi

# Create app directory
WORKDIR /fastapi

# Install app dependencies
RUN pip install -r requirements.txt -f https://download.pytorch.org/whl/torch_stable.html

COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]