from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, DateField, SelectField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    dob = DateField ('Your DOB', format = '%d/%m/%Y')
    age = IntegerField ('age')
    weight = DecimalField ('weight', places=2)
    fav_color = SelectField ('fav colour' ,choices = [('b', 'Blue'), ('R'), ('Red')])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            return f'Thank you {first_name} {last_name}, Your DOB is: {form.dob.data}, Your weight is: {form.weight.data}, and your age is:{form.age.data}'
    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True)

