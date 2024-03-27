<p align="center">
  <img src="https://i.imgur.com/gHDYN8T.png" alt="Project Logo" style="width:220px; height:171px; object-fit:cover;">
</p>

# WebUI for Dockerized Applications

This project provides a simple WebUI for managing a Dockerized application, allowing users to start and stop the container via a web interface. It utilizes Flask for the backend and Docker Python SDK to interact with Docker containers.

## Features

- Start/Stop a specific Docker container using a web interface.
- Password protection for starting/stopping the container.
- Display the current status of the Docker container.

## Requirements

- Docker
- Python 3.10 or newer
- Flask
- Docker Python SDK
- An existing Docker container you wish to control

## Setup Instructions

### Running Without Docker

To run the application without Docker, follow these steps:

1. **Set Up a Python Virtual Environment (Optional but recommended)**

    For linux:

    ```bash
    python3 -m virtualenv venv
    source venv/bin/activate
    ```
    
    For windows:

    ```bash
    python -m virtualenv venv
    venv\Scripts\activate
    ```

2. **Install Dependencies**

    Ensure you are in the project's root directory and run:

    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**

    Create a `.env` file in the root directory of the project and add the following lines:

    ```plaintext
    CONTAINER_NAME=YourContainerName/ID
    PASS=YourPasswordHere
    ```
    Replace `YourContainerName/ID` with your container's name or ID.

    Replace `YourPasswordHere` with a secure password. This will be used to authenticate requests to start or stop the container.

    or

    Instead of a `.env` file, you can export the necessary environment variables in your terminal:

    ```bash
    export CONTAINER_NAME=YourContainerName/ID
    export PASS=YourPasswordHere
    ```

4. **Run the Application**

    Start the Flask application with:

    ```bash
    python3 main.py
    ```

### Running With Docker/Docker Compose

#### Building and Running With Docker

1. **Clone the Repository**

    ```bash
    git clone https://github.com/MortexAG/webui-for-docker-container.git
    cd webui-for-docker-container
    ```

2. **Build the Docker Image**

    ```bash
    docker build -t docker-container-webui .
    ```

3. **Run the Container**

    ```bash
    docker run -d -p 6969:6969 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    --name docker-container-webui docker-container-webui
    ```

4. **Mounting the Container**

    To mount the container to a specific directory:

    ```bash
    docker run -d -p 6969:6969 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /path/to/your/local/data:/data \
    --name docker-container-webui docker-container-webui
    ```

#### Using Docker Compose

Create a `docker-compose.yml` file with the following content:

```yaml
version: '3'
services:
  webui:
    image: docker-container-webui
    container_name: docker-container-webui
    ports:
      - "6969:6969"
    environment:
      PASS: "yourPassword"
      CONTAINER_NAME: "yourContainerName"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    # - /path/to/your/local/data:/data # OPTIONAL
``` 

Then run:

```bash
docker compose up -d
```
## Usage

- Navigate to `http://localhost:6969` in your web browser to access the WebUI.
- To start or stop the Docker container, enter the password set in the `.env` file and click the "Start" or "Stop" button, respectively.
- The status of the container (e.g., running, exited) will be displayed on the web page.

## Notes

- Make sure the container name in the Flask app matches the name of the Docker container you wish to control.
- The application is set to run on port 6969. You can change this by modifying the `app.run` call in the Python script and the `EXPOSE` directive in the Dockerfile.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have feedback or suggestions for improvement.
