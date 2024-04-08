FROM python:3.10.12-alpine

# Set the working directory to /data
WORKDIR /data

# Copy your application files to a different directory in the image
COPY . /data

# Install any dependencies
RUN pip install -r requirements.txt

EXPOSE 6969

CMD ["python3", "main.py"]
