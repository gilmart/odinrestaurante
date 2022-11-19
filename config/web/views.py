from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def PlatosVista(request):
    
    platosConsultados=Platos.objects.all()
    print(platosConsultados)

    
    formulario=FormularioPlatos()
    
    data={
        'formulario':formulario,
        'bandera':False,
        'platos': platosConsultados
    }

    if request.method == 'POST':
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)

            platoNuevo=Platos(
                nombre=datosLimpios['nombre'],
                descripcion=datosLimpios['descripcion'],
                imagen=datosLimpios['imagen'],
                precio=datosLimpios['precio'],
                tipo=datosLimpios['tipo']
                
            )
            #intentar llevar mi datos a la bd
            try:
                platoNuevo.save()
                print("exito guardando") 
                data["bandera"]=True
                print("exito guardando empleado")
            except Exception as error:
                data['bandera']=False
                print("uppps",error)


    return render(request,'menuplatos.html',data)


def EmpleadosVista(request):
    
    formularioEmpleados=FormularioEmpleados()
    data={
        'formularioEmpleados': formularioEmpleados,
        'bandera':False
    }
    if request.method == 'POST':
        datosFormularioEmpleado=FormularioEmpleados(request.POST)
        if datosFormularioEmpleado.is_valid():
            print("es valido")
            datosLimpios=datosFormularioEmpleado.cleaned_data
            print(datosLimpios)

            empleadoNuevo=Empleados(
                nombre=datosLimpios['nombre'],
                apellido=datosLimpios['apellido'],
                imagen=datosLimpios['imagen'],
                cargo=datosLimpios['cargo'],
                salario=datosLimpios['salario'],
                telefono=datosLimpios['telefono'],
                email=datosLimpios['email'],
            )

            try:
                empleadoNuevo.save()
                data["bandera"]=True
                print("exito guardando empleado")
            except Exception as error:
                print("uppps empleado",error)
                data['bandera']=False
        else:
            print("no es valido")
    return render(request,'empleados.html',data)


def EditarMenu(request):
    platosConsultados=Platos.objects.all()
    print(platosConsultados)
    data={
    
        'platos':platosConsultados
    }
    return render(request, 'editarmenu.html',data)

