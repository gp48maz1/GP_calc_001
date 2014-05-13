from flask import render_template
from app import app
from forms import CalcForm

@app.route('/')
@app.route('/index', methods =['GET', 'POST'])
def index():
	#operators = [ ' + ', ' - ', ' * ', ' / ']
	form = CalcForm()
	return render_template("index.html",
		title = 'Home',
		form = form,
		op = form.op.data
		)


#why form = form?