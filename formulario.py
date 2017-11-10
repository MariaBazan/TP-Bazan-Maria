from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms import validators
class Registro(FlaskForm):
    usu = StringField('Usuario', [validators.data_required(message = "Debe ingresar un usuario")])
    passw = PasswordField('Contrasena', [validators.data_required(message = "Debe ingresar una contrasena")])
    usu1 = StringField('Repetir Usuario', [validators.data_required(message = "Debe ingresar un usuario ")])
    passw1 = PasswordField('Repetir Contrasena', [validators.data_required(message = "Debe ingresar una contrasena")])
    submit = SubmitField("Enviar")
class Login(FlaskForm):
    usu = StringField('Usuario', [validators.data_required(message = "Debe ingresar un usuario")])
    passw = PasswordField('Login', [validators.data_required(message = "Debe ingresar una contrasena")])
    submit = SubmitField("Ingresar")
class ConsultaProducto(FlaskForm):
    submit = SubmitField("Buscar")
    producto = StringField('Producto', [validators.data_required(message = "Debe ingresar el nombre del Producto"), validators.Length(min = 3, message = "Debe ingresar como minimo 3 caracteres")])
    submit_selec = SubmitField("Seleccionar")
class Consulta(FlaskForm):
    submit = SubmitField("Aceptar")
    cantidad = IntegerField('Cantidad de items a mostrar', [validators.data_required(message = "Debe ingresar un numero entero")])
class ConsultaCliente(FlaskForm):
    submit = SubmitField("Buscar")
    cliente = StringField('Cliente', [validators.data_required(message = "Debe ingresar el nombre del Cliente"), validators.Length(min = 3, message = "Debe ingresar como minimo 3 caracteres")])
    submit_selec = SubmitField("Seleccionar")
