###Funciones Planilla
import csv
trabajadores=[];
nombreTrabajadores = [];

def registrarTrabajador():
    try: 
        nombre=input("Ingrese el nombre y el apellido del trabajador:  ");
    except ValueError:
        print("Nombre y apellido son obligatorios");
    else:
        try: 
            cargo=input("Ingrese el cargo del trabajador:  ");
        except ValueError:
            print("Ingresar el cargo es obligatorio");
        else:
            try: 
                sueldoBruto=float(input("Ingrese el sueldo del trabajador:  "));
            except ValueError:
                print("Ingresar el sueldo es obligatorio");
            else:
                if(cargo=='CEO'):
                    descSalud=sueldoBruto*0.07 
                    descAfp=sueldoBruto*0.12
                elif(cargo=='Desarrollador'):   
                    descSalud=sueldoBruto*0.05 
                    descAfp=sueldoBruto*0.10
                elif(cargo=='Analista'):
                    descSalud=sueldoBruto*0.06
                    descAfp=sueldoBruto*0.11  

    nombreTrabajadores.append(nombre);
    liquidoPagar=(sueldoBruto-descSalud-descAfp);

    trabajador = {
    'nombre': nombre,
    'cargo': cargo,
    'sueldoBruto': sueldoBruto,
    'descSalud': descSalud,
    'descAfp': descAfp,
    'liquidoPagar': liquidoPagar
    }
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente.\n")
    print(trabajadores)
    




