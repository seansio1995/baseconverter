##Convert number into any base
from flask import Flask, render_template, request
from math import pow
from wtforms import Form,FloatField,IntegerField, validators
from converter import baseConverter

app=Flask(__name__)

class InputForm(Form):
    number=IntegerField(validators=[validators.InputRequired()])
    base=IntegerField(validators=[validators.InputRequired()])


@app.route('/baseconverter',methods=["GET","POST"])

def index():
    form=InputForm(request.form)
    if request.method=="POST" and form.validate():
        number=form.number.data
        base=form.base.data

        result=baseConverter(number,base)
        return render_template("output.html",form=form,result=result)
    else:
        return render_template("input.html",form=form)


if __name__=="__main__":
    app.run(debug=True)
