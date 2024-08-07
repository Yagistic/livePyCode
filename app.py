"""
Flask Live Code </>

"""
from flask import (
	Flask,
	render_template,
	redirect,
	url_for,
	request)
import subprocess
import os 
import sys


app = Flask(__name__)
path = os.getcwd()
tmpFile = os.path.join(path,"temp")

@app.route("/", methods= ["GET", "POST"])
def home():
	code = ""
	output = ""
	if request.method == "POST":
		code = request.form["code"]
		try:
			output = subprocess.check_output([sys.executable ,"-c", code]).decode("utf-8")
			
		except Exception as ex:
			output = ex
			
	return render_template("main.html",output=output, code=code)
	
	
if __name__ == "__main__":
	app.run(debug=True)
	