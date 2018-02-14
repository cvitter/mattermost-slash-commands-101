from flask import Flask

__doc__ = """\
ping.py

"""

app = Flask(__name__)

@app.route("/ping")
def ping():
        return "Pong!"

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug = False)
