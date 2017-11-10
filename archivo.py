import csv

class Error (Exception) :
    pass
def grabar(archivo, dato1, dato2) :
    with open(archivo,  "a") as salidacsv:
        campos = ['login', 'usuario']
        salida = csv.DictWriter(salidacsv,lineterminator='\n', fieldnames = campos)
        salida.writerow({'login': dato1, 'usuario': dato2})

def lista_producto(archivo1):
    with open(archivo1) as archivo:
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['PRODUCTO'] not in lista_consulta:
                lista_consulta.append(l['PRODUCTO'])
        return lista_consulta

def leer(archivo1) :
    with open(archivo1) as archivo :
         arch_csv = csv.DictReader(archivo)
         listadic = list(arch_csv)
         return listadic

def lista_clientes(archivo1) :
    with open(archivo1) as archivo :
        arch_csv = csv.DictReader(archivo)
        listadic = list(arch_csv)
        lista_consulta = []
        for l in listadic :
            if l['CLIENTE'] not in lista_consulta :
               lista_consulta.append(l['CLIENTE'])
        return lista_consulta

def validar(archivo) :
    try:
        with open(archivo) as archivo:
            arch_csv = csv.DictReader(archivo)
            listadic = list(arch_csv)
            msj = False

            for item in listadic :
                if len(item) != 5 :
                    raise Error("verifique el nro de columnas del archivo")

                if type(int(item['CODIGO'])) != int and item['CODIGO'] is not None :
                   pass
                else :
                    msj = True

                if str(item['PRODUCTO']).isnumeric():
                    raise Error("el campo no debe contener numeros")
                else :
                    msj = True

                if str(item['CLIENTE']).isnumeric():
                    raise Error("el campo no debe contener numeros")
                else :
                    msj = True

                if float(item['CANTIDAD']) % 1 == 0 :
                    msj = True
                else :
                    raise Error("La cantidad debe ser un numero entero")

                if float(item['PRECIO']) % 1 == 0 or float(item['PRECIO']) % 1 != 0 :
                     msj = True
                else:
                    raise Error("El precio debe ser un numero")
        if msj:
             return True

    except Error as error :
        print(error)
        print("")
        print("-No se puede procesar el archivo-")
    except ValueError:
        print("error en el tipo de valor del campo")
        print("")
        print("-No se puede procesar el archivo-")
    except FileNotFoundError:
        print("No se puede leer el archivo")
        print("")
        print("-No se puede procesar el archivo-")





