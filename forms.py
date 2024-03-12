from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField,RadioField,EmailField,IntegerField,SelectMultipleField,BooleanField,DateField
from wtforms import EmailField
from wtforms import validators



class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField("nombre",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=10,message='ingresa nombre valido')])
    
    apaterno=StringField('apaterno',[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=10,message='ingresa apellido valido')])
    
    amaterno=StringField('amaterno',[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=10,message='ingresa apellido valido')])
    
    direccion=StringField('direccion',[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=50,message='ingresa domicilio valido')])

    edad=IntegerField('edad',
                      [validators.number_range(min=1, message='valor no valido')])

    email=EmailField('correo',[
        validators.Email(message='Ingrese un correo valido'
                         )])
  
class BusquedaOrden(Form):
    busqueda=StringField("nombre",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=1,max=10,message='ingresa nombre valido')])

class PizzaForm(Form):
    
    nombre=StringField("nombre",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=50,message='ingresa nombre valido')])
    direccion=StringField("direccion",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=50,message='ingresa direccion valido')])
    telefono=StringField("telefono",[validators.DataRequired(message='el campo es requerido'),
                                 validators.length(min=4,max=10,message='ingresa telefono valido')])
    tamañoPizza=RadioField("tamaño Pizza", 
                                    choices=[('chica','Chica $40'),('mediana','Mediana $80'),('grande','Grange $120')],
                                            validators=[validators.DataRequired(message='El campo es requerido')])
    
    jamon = BooleanField('Jamon $10', default=False)
    piña = BooleanField('Piña $10', default=False)
    champiñones = BooleanField('Champiñones $10', default=False)
    numeroPizza=IntegerField("Numero de Pizzas",[validators.number_range(min=1, message='valor no valido')])
    fecha = DateField("Fecha", format='%Y-%m-%d', validators=[validators.DataRequired(message='El campo es requerido')])

    
