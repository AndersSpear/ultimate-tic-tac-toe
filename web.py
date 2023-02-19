import os
from base64 import b64encode
from flask import Flask, render_template
from flask_discord import DiscordOAuth2Session
from importlib import import_module
from threading import Thread

#sets up a flask application
app = Flask('')
app.url_map.strict_slashes = False
app.jinja_env.filters['debug'] = lambda x: print(x) or ''

@app.route('/')
def index():
    return render_template('index.html')

def run():
    #runs the webserver in a separate thread
    thread = Thread(target=lambda: app.run('0.0.0.0'))
    thread.start()
