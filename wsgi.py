from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Greetings Earth!  OpenShift Hello World by AubreyR. Testing Git push via IDE (vscode)."

if __name__ == "__main__":
    application.run()
