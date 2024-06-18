###Funciones Planilla
import csv
trabajadores=[];

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
                sueldoBruto=int(input("Ingrese el sueldo del trabajador:  "));
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
    return;
    
def mostrarlista():
    print(f"Trabajador: {nombre} Cargo");



def imprimirPlanilla():
    if not trabajadores:
        print("No se encuentran trabajadores registrados.")
        return
    
    print("\n¿De quién desea imprimir la planilla?")
    decisionPlanilla = input("\n1.- CEO\n2.- Desarrollador\n3.- Analista\nIngrese su decisión: ")

    if decisionPlanilla == '1':
        cargo = 'CEO'
    elif decisionPlanilla == '2':
        cargo = 'Desarrollador'
    elif decisionPlanilla == '3':
        cargo = 'Analista'
    else:
        print("Opción no válida")
        return

    with open(f"Planilla_Trabajadores_{cargo}.txt", 'w') as planilla_trabajadores:
        for trabajador in trabajadores:
            if trabajador['cargo'] == cargo:
                planilla_trabajadores.write(f"Nombre: {trabajador['nombre']}, Cargo: {trabajador['cargo']}, Sueldo Bruto: {trabajador['sueldoBruto']}, Desc. Salud: {trabajador['descSalud']}, Desc. AFP: {trabajador['descAfp']}, Líquido a Pagar: {trabajador['liquidoPagar']}\n")
                print(f"Planilla de sueldos para el cargo {cargo} generada exitosamente.")
    
    print(f"\nContenido de la planilla para el cargo {cargo}:\n")
    try:
        with open(f"Planilla_Trabajadores_{cargo}.txt", 'r') as planilla_trabajadores:
            contenido = planilla_trabajadores.read()
            print(contenido)
    except FileNotFoundError:
        print(f"No se encontró la planilla para el cargo {cargo}. Verifique que haya sido generada previamente.")








