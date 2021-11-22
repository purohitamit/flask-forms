from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, IntegerField,SelectField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    D_O_B = DateField('Date Of Birth', format='%Y/%m/%d')
    fav_num = IntegerField('Your Favourite Number')
    fav_food = SelectField('Your Favourite food', choices = [('pizza', 'Pizza'), ('chicken', 'Chicken'), ('paneer', 'Paneer')])
    submit = SubmitField('Generate Username')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    #if request.method == 'POST':
        

    return render_template('home.html', form=form, message=message)


if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')

