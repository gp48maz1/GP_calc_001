from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, RadioField
from wtforms.validators import Required

class CalcForm(Form):
	num01 = TextField('num01', validators = [Required()])
	num02 = TextField('num02', validators = [Required()])
	op = RadioField('op', choices=[('+','+'),('-','-'),('*','*'),('/','/')])

#how do I make the radio button default to one specific one?
#how would Ihave made a drop down?