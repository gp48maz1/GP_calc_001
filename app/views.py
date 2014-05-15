from flask import render_template, request
from app import app
from forms import CalcForm

app.debug = True

@app.route('/', methods = ['GET', 'POST'])

@app.route('/about', methods = ['GET'])
def about():
	return render_template("about.html",
		title='About'
		)

@app.route('/index', methods =['GET', 'POST'])
def index():
	#operators = [ ' + ', ' - ', ' * ', ' / ']

	form = CalcForm()
	if request.method == 'POST':
		try :
			num01 = float(form.num01.data)
			num02 = float(form.num02.data)
		except:
			return render_template("index.html", 
				answer = "",
				form = form,
				error = "Error, non-numerical input.")

		answer = None

		op = form.op.data
		print('result: ',num01, num02, op)
		if op == '+':
			answer = num01 + num02
		elif op == '-':
			answer = num01 - num02
		elif op == '*':
			answer = num01 * num02
		elif op == '/':
			answer = num01 / num02
		else:
			answer="wrong"

		return render_template("index.html",
			title = 'Home', 
			answer=answer, 
			form = form,
			error="")
	else:
		#otherwise it is a get and i just want to render the template
		return render_template("index.html",
			title = 'Home',
			form = form,
			answer = "")
		"""
		return render_template("index.html",
			title = 'Home',
			form = form,
			num01 = form.num01.data,
			op = form.op.data,
			num02 = form.num02.data,
			answer = form.num02.data
			)
	"""

#block comment out command+/

#why form = form?

#form.whatever.data ==> wtf
#request.form.get("whatever") ==> html??