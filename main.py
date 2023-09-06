# CODIGO JESÚS DAVID GUZMÁN GONZÁLEZ
class Paciente:
    # Constructor de la clase paciente
    def __init__(self, documento, nombre,
                 sexo, fecha_nacimiento):
        self.documento = documento
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento

    # Método para mostrar la información de un paciente registrado
    def mostrar_informacion(self):
        print(f"Documento: {self.documento}")
        print(f"Nombre: {self.nombre}")
        print(f"Sexo: {self.sexo}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")


class Signos_vitales:
    # Constructor de la clase signos vitales
    def __init__(self, presion_arterial, temperatura,
                 saturacionO2, frecuencia_respiratoria):
        self.presion_arterial = presion_arterial
        self.temperatura = temperatura
        self.saturacionO2 = saturacionO2
        self.frecuencia_respiratoria = frecuencia_respiratoria

    # Método para mostrar la información de signos vitales de un paciente registrado
    def mostrar_signos_vitales(self):
        print(f"Presión arterial: {self.presion_arterial}")
        print(f"Temperatura: {self.temperatura}")
        print(f"Saturación de O2: {self.saturacionO2}")
        print(f"Frecuencia respiratoria: {self.frecuencia_respiratoria}")


# Método estático para registrar un paciente
def registrar_paciente():
    documento = input("Ingrese documento del apciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    opcion = int(input("Ingrese sexo del paciente:"
                       "\n1)Masculino"
                       "\n2)Femenino"
                       "\nR. "))
    # Ciclo while encargado de validación de datos
    while opcion != 1 and opcion != 2:
        print("Opción incorrecta, elija de nuevo")
        opcion = int(input("Ingrese sexo del paciente:"
                           "\n1)Masculino"
                           "\n2)Femenino"
                           "\nR. "))
    if opcion == 1:
        sexo = "Masculino"
    else:
        sexo = "Femenino"

    fecha_nacimiento = input("Ingrese la fecha de nacimiento DD/MM/AA: ")

    paciente = Paciente(documento, nombre, sexo, fecha_nacimiento)
    personas_registradas.append(paciente)

    print("Paciente registrado exitosamente...")


# Método estático para registrar los signos vitales de un paciente
def registrar_signos_vitales():
    presion_arterial = input("Ingrese la presión arterial: ")
    temperatura = input("Ingrese la temperatura: ")
    saturacionO2 = input("Ingrese la saturación de O2: ")
    frecuencia_respiratoria = input("Ingrese la frecuencia respiratoria: ")

    signos = Signos_vitales(presion_arterial, temperatura, saturacionO2, frecuencia_respiratoria)

    signos_vitales.append(signos)

    nota = input("NOTAS ADICIONALES DE EVOLUCION: ")
    medicamento = input("INGRESE LOS MEDICAMENTOS FORMULADOS SEGUIDOS POR COMAS: ")

    notas.append(nota)
    medicamentos.append(medicamento)


# Método para buscar paciente por documento
def buscar_paciente_por_documento(documento):
    # Ciclo for encargado de buscar el documento del paciente e imprimir la información del paciente que coincida
    # todo con respecto a una posición
    for i in range(len(personas_registradas)):
        if documento.lower() == personas_registradas[i].documento.lower():
            print(personas_registradas[i].mostrar_informacion())
            print(signos_vitales[i].mostrar_signos_vitales())
            print("Notas de evolucion: ", notas[i])
            print("Medicamentos formulados: ", medicamentos[i])
            return 0
    print("No se encontró ningún paciente con ese documento...")
    return 0


personas_registradas = []
signos_vitales = []
notas = []
medicamentos = []

# Ciclo principal, para iterar n veces hasta que el usuario lo desee.
while True:
    eleccion = int(input("Bienvenido al sistema de gestión de pacientes del Hispital San Vicente"
                         "\nElija una opción:"
                         "\n1)Registrar un paciente"
                         "\n2)Consultar un paciente"
                         "\n3)Cerrar sesión"
                         "\nR. "))

    if eleccion == 1:
        registrar_paciente()
        registrar_signos_vitales()

    elif eleccion == 2:
        documento = input("Ingrese el documento del paciente: ")
        buscar_paciente_por_documento(documento)

    elif eleccion == 3:
        print("Saliendo...")
        break
