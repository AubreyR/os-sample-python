from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Greetings Earth!  OpenShift Hello World by AubreyR"

if __name__ == "__main__":
    application.run()
