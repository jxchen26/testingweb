from flask import Flask, render_template, request, redirect,url_for, session 
from myforms import Form1, HittingForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "not a Secret"


#home page
@app.route("/", methods = ["GET","POST"])
def helloworld():

	if "moreforms" not in session:
		print("new session is created!")
		session["moreforms"] = 0 

	# #prevent the user from ever getting more than 10 forms 
	hitforms = Form1() # starts with one hitform entry

	# print("NUM:", session["number_of_forms"])
	if request.method == "GET":
		for i in range(session["moreforms"]):
			hitform = HittingForm()

			#an error will occur when the user trys to add more than max forms 
			try:
				hitforms.forms.append_entry(hitform) # adds a hitform into form1
			except:
				break #stop adding more forms

		return render_template("home.html", f = hitforms)

	if request.method == "POST" and hitforms.validate_on_submit():
		data1 = request.form.to_dict(flat=False)
		print(data1)
		print(type(data1))
		return render_template("home.html",data = "Form submitted", f = hitforms)

#flask has client side sessions, where data is stored on the client side.
#but the coookie is crytographically signed 
#and cannot store more than 4KB of data 
@app.route("/+",methods = ["POST"])
def add():
	try: 
		if "moreforms" in session:
			session["moreforms"] += 1 
	except:
		return

	return redirect (url_for('helloworld'))



@app.route("/-",methods = ["POST"])
def sub():
	try: 
		if "moreforms" in session:
			session["moreforms"] -= 1 
	except:
		return	

try:
    app.run(debug=True)
except Exception as e:
    print(f"the following error occur when trying to start flask app: {e}")
