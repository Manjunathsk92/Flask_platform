from flask import render_template
from flask_platform import flask_platform
from systeminfo import main as m

@flask_platform.route('/')
def index():
        returnDict = {}
        returnDict['platform'] = m.main()
        return render_template("index.html", **returnDict)
