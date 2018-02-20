from flask import Flask

__doc__ = """\
ping.py
   Basic flask application to respond to a slash command in Mattermost
"""

app = Flask(__name__)

@app.route("/ping")
def ping():
        return "Pong!"

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = False)
