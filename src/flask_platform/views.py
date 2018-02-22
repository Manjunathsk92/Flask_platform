from flask import render_template
from flask_platform import flask_platform
import systeminfo

@flask_platform.route('/')
def index():
        returnDict = {}
        returnDict['platform'] = systeminfo.main()
        return render_template("index.html", **returnDict)
