FROM python:3.10.12-alpine

# Set the working directory to /data
WORKDIR /data

# Copy your application files to a different directory in the image
COPY . /data_original

# Install any dependencies
RUN pip install -r /data_original/requirements.txt

# Copy the entrypoint script to the root and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 6969

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "main.py"]
