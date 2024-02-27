from flask import Flask, request,render_template,Response
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g 
from config import DevelopmentConfig
from flask import flash
from models import db
from models import Maestros
app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/index",methods=["GET","POST"])
def index():
    maestro_form=forms.UserForm(request.form)
    if request.method=='POST' and maestro_form.validate():
        maestro=Maestros(nombre=maestro_form.nombre.data,
                    apaterno=maestro_form.apaterno.data,
                    amaterno=maestro_form.amaterno.data,
                    edad=maestro_form.edad.data,
                    direccion=maestro_form.direccion.data,
                    email=maestro_form.email.data)
        db.session.add(maestro)
        db.session.commit()
    return render_template("index.html", form=maestro_form)


@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
    maestro=""
    
  
    maestro=Maestros.query.all()
    return render_template("ABC_Completo.html",maestros=maestro)


if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.run()

