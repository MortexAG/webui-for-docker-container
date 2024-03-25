import flask
from flask import Flask, request, render_template, jsonify
import docker
#import threading
#from threading import Thread
import os
import dotenv 
from dotenv import load_dotenv

load_dotenv()

password = os.environ['PASS']
container_name = os.environ['CONTAINER_NAME']

client = docker.from_env()
app = Flask(__name__, template_folder = "templatefiles", static_folder= "staticfiles")


@app.route('/status')
def get_status():
    try:
        bot_status_var = check_container_status(container_name)
        return jsonify({'status': bot_status_var}), 200
    except Exception as e:
        return jsonify({'status':str(e)}), 500

@app.route('/start', methods=['POST'])
def start_bot():
    try:
        if str(request.form['password']) == str(password):
            container = client.containers.get(container_name)
            container.start()
            # in this json {"status":200} can literally be anythig like {"mort":"good"} and on the jquery side it will be data.mort === "good"
            return jsonify({'status': 200}), 200
        else:
            return jsonify({'status': "Wrong Password"})
    except Exception as e:
        return jsonify({"status":str(e)}), 500

@app.route('/stop', methods=['POST'])
def stop_bot():
    try:
        if str(request.form['password']) == str(password): 
            container = client.containers.get(container_name)
            container.stop()
            return jsonify({'status': 200}), 200
        else:
            return jsonify({'status': "Wrong Password"})
    except Exception as e:
        return jsonify({"status":str(e)}) ,500

def check_container_status(container_name):
    container = client.containers.get(container_name)
    status = container.status
    return status
    #return container

@app.route("/")
def main():

    bot_status_var = check_container_status(container_name)
    return render_template("index.html", bot_status = bot_status_var, container_name = container_name)


def run():
  app.run(
    host="0.0.0.0",
    port=6969
  )

#def keep_alive():
#  t = Thread(target=run)
#  t.start()

#keep_alive()
run()

