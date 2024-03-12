from datetime import date
from datetime import datetime
from flask import Flask, request,render_template,Response
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g 
from config import DevelopmentConfig
from flask import flash
from models import db
from models import Maestros
from models import Pizza
from models import PizzaOrden
from models import Venta

from io import open
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
        print(maestro_form.nombre.data)
        db.session.add(maestro)
        db.session.commit()
    return render_template("index.html", form=maestro_form)


@app.route("/ABC_Completo",methods=["GET","POST"])
def ABCompleto():
    maestro=""
    
  
    maestro=Maestros.query.all()
    return render_template("ABC_Completo.html",maestros=maestro)

@app.route("/Ventas",methods=["GET","POST"])
def Ventas():
    ventas=""

    ventas_por_dia_semana = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }



    
  
    ventas=Pizza.query.all()
    
    for venta in ventas:
        print(venta)
        dia_semana = venta.create_date.strftime("%A")
        if dia_semana in ventas_por_dia_semana:
            
            ventas_por_dia_semana[dia_semana].append(venta)


    return render_template("Ventas.html",Ventas=ventas,
                            lunes = ventas_por_dia_semana["Monday"],
                            martes = ventas_por_dia_semana["Tuesday"],
                            miercoles = ventas_por_dia_semana["Wednesday"],
                            jueves = ventas_por_dia_semana["Thursday"],
                            viernes = ventas_por_dia_semana["Friday"],
                            sabado = ventas_por_dia_semana["Saturday"],
                            domingo = ventas_por_dia_semana["Sunday"])

@app.route("/ventaBusqueda",methods=["GET","POST"])
def ventaBusqueda():
    dias_espanol_ingles = {
        "lunes": "Monday",
        "martes": "Tuesday",
        "miercoles": "Wednesday",
        "miércoles": "Wednesday",
        "jueves": "Thursday",
        "viernes": "Friday",
        "sabado": "Saturday",
        "sábado": "Saturday",
        "domingo": "Sunday"
    }
   
    # Diccionario de nombres de mes en español a inglés
    meses_espanol_ingles = {
        "enero": "January",
        "febrero": "February",
        "marzo": "March",
        "abril": "April",
        "mayo": "May",
        "junio": "June",
        "julio": "July",
        "agosto": "August",
        "septiembre": "September",
        "octubre": "October",
        "noviembre": "November",
        "diciembre": "December"
    }
    

    buscar=""
    busquedaIngles=""
    TOTALBUSQUEDA=0
    listaBuscar=[]
    busqueda_form=forms.BusquedaOrden(request.form)
    if request.method=='POST'  and busqueda_form.validate and "ordenar" in request.form:
        busqueda=busqueda_form.busqueda.data
        busquedaLower=busqueda.lower()
        print(busquedaLower)
        if busquedaLower in meses_espanol_ingles:
            busquedaIngles=meses_espanol_ingles.get(busquedaLower)
            print(busquedaIngles)
            buscar = Venta.query.all()
            
            for item in buscar:
                print(item)
                
                mes = item.create_dateVenta.strftime("%B")
                print(mes)
                if mes==busquedaIngles:
                    TOTALBUSQUEDA=TOTALBUSQUEDA+int(item.totalVenta)
                    listaBuscar.append(item)
            
                
        

        elif busquedaLower in dias_espanol_ingles:
            busquedaIngles=dias_espanol_ingles.get(busquedaLower)
            print(busquedaIngles)
            buscar = Venta.query.all()
            
            for item in buscar:
                print(item)
                
                dia_semana = item.create_dateVenta.strftime("%A")
                print(dia_semana)
                if dia_semana==busquedaIngles:
                    TOTALBUSQUEDA=TOTALBUSQUEDA+int(item.totalVenta)
                    listaBuscar.append(item)

        else:
            buscar=Venta.query.filter(
                (Venta.nombreVenta.like(f"%{busqueda}%")) |
                (Venta.telefonoVenta.like(f"%{busqueda}%")) |
                (Venta.totalVenta.like(f"%{busqueda}%")) |
                (Venta.create_dateVenta.like(f"%{busqueda}%"))
            )
            for item in buscar:
                    listaBuscar.append(item)
                    TOTALBUSQUEDA=TOTALBUSQUEDA+int(item.totalVenta)

          
    print("TOTAL BUS")
    print(TOTALBUSQUEDA)
            
                
        




    return render_template("ventasBusqueda.html",form=busqueda_form,busqueda=listaBuscar,TOTALBUSQUEDA=TOTALBUSQUEDA)

@app.route("/VentasMes",methods=["GET","POST"])
def VentasMes():
   

    ventas_por_mes = {
        "January": [],
        "February": [],
        "March": [],
        "April": [],
        "May": [],
        "June": [],
        "July": [],
        "August": [],
        "September": [],
        "October": [],
        "November": [],
        "December": []
    }

    ventas = Pizza.query.all()

    for venta in ventas:
        mes = venta.create_date.strftime("%B")  
        if mes in ventas_por_mes:
            ventas_por_mes[mes].append(venta)



    return render_template("VentasPorMes.html",Ventas=ventas,
                            enero = ventas_por_mes["January"],
                            febrero = ventas_por_mes["February"],
                            marzo = ventas_por_mes["March"],
                            abril = ventas_por_mes["April"],
                            mayo = ventas_por_mes["May"],
                            junio = ventas_por_mes["June"],
                            julio = ventas_por_mes["July"],
                            agosto = ventas_por_mes["August"],
                            septiembre = ventas_por_mes["September"],
                            octubre = ventas_por_mes["October"],
                            noviembre = ventas_por_mes["November"],
                            diciembre = ventas_por_mes["December"])

formulario=forms.PizzaForm()
@app.route("/pizzeria",methods=["GET","POST"])
def pizzeria():
    pizza_form=forms.PizzaForm(request.form)
    global formulario
    
    pizzaOrden=""
    archivo_texto=""
    pizzaOrdenes=[]

    ventas=""
    TotalDia=0
    fecha_actual = date.today()
  
    ventas=Pizza.query.filter(db.func.date(Pizza.create_date) == fecha_actual).all()

    
    ventas_hoy = Pizza.query.filter(db.func.date(Pizza.create_date) == fecha_actual).all()
    if ventas_hoy:
        # Sumar los subtotales de las ventas del día en curso
        TotalDia = sum(venta.subtotal for venta in ventas_hoy)
    else:
        TotalDia = 0  # No hay ventas, por lo tanto, el total es cero

    
    
    if "terminarOrden" in request.form:
   
        total=0
        
        archivo_texto=open('orden.txt','r')
        i=1    
        nombreV=""
        telefonoV=""
        direccionV=""
        fechaV=""
        for lineas in archivo_texto.readlines():
            indexTxt=i
            if  lineas.strip():
                
                nombreBD,direccionBD,telefonoBD,tamañoBD,ingredientesBD,numeroPizzaBD,subtotalBD,fechaBD=lineas.split(':')
                nombreV=nombreBD
                telefonoV=telefonoBD
                fechaV=fechaBD
                direccionV=direccionBD
                total=total+int(subtotalBD)
                ordenes=Pizza(nombre=nombreBD,direccion=direccionBD,telefono=telefonoBD,
                              tamaño=tamañoBD,ingredientes=ingredientesBD,numeroPizza=numeroPizzaBD,subtotal=subtotalBD,create_date=fechaBD)
                db.session.add(ordenes)
                db.session.commit()
                
                i=i+1
                archivo_texto.close()
        print(nombreV, direccionV, telefonoV, total, fechaV)
        ventas = Venta(nombreVenta=nombreV, direccionVenta=direccionV, telefonoVenta=telefonoV, totalVenta=total, create_dateVenta=fechaV)
        db.session.add(ventas)
        db.session.commit()


        
        with open('orden.txt', 'w') as archivo:
                archivo.write('')
        ventas=Pizza.query.filter(db.func.date(Pizza.create_date) == fecha_actual).all()
        ventas_hoy = Pizza.query.filter(db.func.date(Pizza.create_date) == fecha_actual).all()
        if ventas_hoy:
        # Sumar los subtotales de las ventas del día en curso
            TotalDia = sum(venta.subtotal for venta in ventas_hoy)
        else:
            TotalDia = 0  # No hay ventas, por lo tanto, el total es cero
        

    

    if "quitarOrden" in request.form:
        with open('orden.txt', 'w') as archivo:
                archivo.write('')
        datos= request.form.get("datos")    
        datos= request.form.get("datos")
        print("LONGITUD")
        print(len(datos))
        if len(datos)>0:

            datos[0].split('[')
            datos[0].split(']')
       
            datos_lista = datos.split(':')
            resultados = []

            for dato in datos_lista:
                partes = dato.split(':')
                resultados.extend(partes)

            resultados2=[]
        
            for elemento in datos_lista:
                partes=elemento.split('/')
                resultados2.append(partes)
            
            pizzaOrd=""
            i=0
            if resultados2[-1] == ['']:
                resultados2.pop()
        
            with open('orden.txt', 'w') as archivo:
                archivo.write('')
            for orden in resultados2:
            
            
                archivo_texto=open('orden.txt','a')
                print("QUEEEEEEEEEEEEEEEE?")
                print(resultados[i][7])
            
                archivo_texto.write('\n'+resultados2[i][4]+':'+resultados2[i][5]+':'+resultados2[i][6]+':'
                                +resultados2[i][0]+':'+resultados2[i][1]+':'
                                +resultados2[i][2]+':'+resultados2[i][3]+':'+resultados2[i][7])
        
        
                archivo_texto.close()
            
            
                i=i+1
            

            
            
                
                

        
        
    if request.method=='POST'  and pizza_form.validate and "ordenar" in request.form:
        
        formulario=pizza_form

        nombre=pizza_form.nombre.data
        direccion=pizza_form.direccion.data
        telefono=pizza_form.telefono.data
        tamaño=pizza_form.tamañoPizza.data
        piña=pizza_form.piña.data
        jamon=pizza_form.jamon.data
        champiñones=pizza_form.champiñones.data
        numeroPizza=pizza_form.numeroPizza.data
        
        fecha=pizza_form.fecha.data
        fecha_str=str(fecha)
        fecha_seleccionada = datetime.strptime(fecha_str, '%Y-%m-%d')

        print("FECHA")

  
        print(fecha)
        print(fecha_seleccionada.day)
        print(fecha_seleccionada.month)
        print(fecha_seleccionada.year)
        fecha_dia_con_cero=""
        fecha_mes_con_cero=""
        if fecha_seleccionada.day<10:
            fecha_dia_con_cero="0"+str(fecha_seleccionada.day)
        else :
            fecha_dia_con_cero=str(fecha_seleccionada.day)

        if fecha_seleccionada.month<10:
            fecha_mes_con_cero="0"+str(fecha_seleccionada.month)
        else:
            fecha_mes_con_cero=str(fecha_seleccionada.month)
        print("dia con cero")
        print(fecha_dia_con_cero)

        costoIngredientes=0
        costoTamaño=0
        subtotal=0
        ingredientes=" "
        if piña:
            
            ingredientes=ingredientes+" piña-"
            costoIngredientes=costoIngredientes+10
        if jamon:
            
            ingredientes=ingredientes+" jamon-"
            costoIngredientes=costoIngredientes+10
        if champiñones:
            ingredientes=ingredientes+" champiñones"
            costoIngredientes=costoIngredientes+10
        
        if tamaño=='chica':
            costoTamaño=40
        elif tamaño=='mediana':
            costoTamaño=80
        elif tamaño=='grande':
            costoTamaño=120

        subtotal=numeroPizza*(costoTamaño+costoIngredientes)
        print("SubTOTAL")
        print(subtotal)
        
        archivo_texto=open('orden.txt','a')

        tamaño_str=str(tamaño)
        numeroPizza_str=str(numeroPizza)
        subtotal_str=str(subtotal)
        archivo_texto.write('\n'+nombre+':'+direccion+':'+telefono+':'+tamaño_str+':'+ingredientes+':'
                            +numeroPizza_str+':'+subtotal_str+':'+str(fecha_seleccionada.year)+'-'+str(fecha_mes_con_cero)+'-'+str(fecha_dia_con_cero))
        '''+str(fecha_seleccionada)+':'
        '''
        
        archivo_texto.close()

        

    archivo_texto=open('orden.txt','r')
    i=1    

    #variables para formulario
    nombreForm=""
    direccionForm=""
    telefonoForm=""
    
    
    numeroPizzaForm=""
    fechaForm=""

    #
    for lineas in archivo_texto.readlines():
        indexTxt=i
        if  lineas.strip():
            nombreTxt,direccionTxt,telefonoTxt,tamañoTxt,ingredientesTxt,numeroPizzaTxt,subtotalTxt,fechaTxt=lineas.split(':')
            pizzaOrden=PizzaOrden(nombreTxt,direccionTxt,telefonoTxt,tamañoTxt,ingredientesTxt,numeroPizzaTxt,subtotalTxt,fechaTxt)
            #
            nombreForm=nombreTxt
            direccionForm=direccionTxt
            telefonoForm=telefonoTxt
    
    
            numeroPizzaForm=numeroPizzaTxt
            fechaForm=fechaTxt
            print("fecha formulario")
            print(fechaTxt)
            #
            pizzaOrdenes.append(pizzaOrden)
            i=i+1
            archivo_texto.close()

    return render_template("pizzeria.html",form=formulario,ordenes=pizzaOrdenes, ventas=ventas,TotalDia=TotalDia,
    nombreForm=nombreForm,
    direccionForm=direccionForm,
    telefonoForm=telefonoForm,
    numeroPizzaForm=numeroPizzaForm,
    fechaForm=fechaForm
    )


if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    app.run()

