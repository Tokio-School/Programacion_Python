from datetime import datetime


class Especialidad:

    def __init__(self, id_especialidad, nombre, coste_base):
        self.id_especialidad = id_especialidad
        self.nombre = nombre
        self.coste_base = coste_base

    @property
    def id_especialidad(self):
        return self.__id_especialidad

    @id_especialidad.setter
    def id_especialidad(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID de la especialidad debe ser un entero positivo")
        self.__id_especialidad = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre de la especialidad no puede estar vacío")
        self.__nombre = valor.strip()

    @property
    def coste_base(self):
        return self.__coste_base

    @coste_base.setter
    def coste_base(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El coste base debe ser un número positivo")
        self.__coste_base = float(valor)

    def mostrar_info(self):
        return f"Especialidad [{self.id_especialidad}] - {self.nombre} | Coste base: {self.coste_base:.2f}€"


class Medico:

    def __init__(self, id_medico, nombre, especialidad, numero_colegiado, activo=True):
        self.id_medico = id_medico
        self.nombre = nombre
        self.especialidad = especialidad
        self.numero_colegiado = numero_colegiado
        self.activo = activo
        self.citas = []

    @property
    def id_medico(self):
        return self.__id_medico

    @id_medico.setter
    def id_medico(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del médico debe ser un entero positivo")
        self.__id_medico = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del médico no puede estar vacío")
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError("El nombre del médico debe tener al menos 3 caracteres")
        self.__nombre = valor

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not isinstance(valor, Especialidad):
            raise TypeError("La especialidad debe ser un objeto de la clase Especialidad")
        self.__especialidad = valor

    @property
    def numero_colegiado(self):
        return self.__numero_colegiado

    @numero_colegiado.setter
    def numero_colegiado(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de colegiado no puede estar vacío")
        self.__numero_colegiado = valor.strip().upper()

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado activo debe ser booleano")
        self.__activo = valor

    def agregar_cita(self, cita):
        if not isinstance(cita, Cita):
            raise TypeError("Solo se pueden agregar objetos de tipo Cita")
        self.citas.append(cita)

    def tiene_cita_en_fecha(self, fecha_hora):
        return any(
            cita.fecha_hora == fecha_hora and cita.estado not in ["cancelada"]
            for cita in self.citas
        )

    def mostrar_info(self):
        return (
            f"Médico [{self.id_medico}] - {self.nombre} | "
            f"Especialidad: {self.especialidad.nombre} | "
            f"Colegiado: {self.numero_colegiado} | Activo: {self.activo}"
        )


class Paciente:

    def __init__(self, id_paciente, nombre, edad, dni, tiene_seguro=False):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.tiene_seguro = tiene_seguro
        self.historial = HistorialClinico(self)
        self.citas = []

    @property
    def id_paciente(self):
        return self.__id_paciente

    @id_paciente.setter
    def id_paciente(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del paciente debe ser un entero positivo")
        self.__id_paciente = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del paciente no puede estar vacío")
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError("El nombre del paciente debe tener al menos 3 caracteres")
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or valor < 0 or valor > 120:
            raise ValueError("La edad debe estar entre 0 y 120 años")
        self.__edad = valor

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 5:
            raise ValueError("El DNI no tiene un formato válido")
        self.__dni = valor.strip().upper()

    @property
    def tiene_seguro(self):
        return self.__tiene_seguro

    @tiene_seguro.setter
    def tiene_seguro(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El campo tiene_seguro debe ser booleano")
        self.__tiene_seguro = valor

    def agregar_cita(self, cita):
        if not isinstance(cita, Cita):
            raise TypeError("Solo se pueden agregar objetos de tipo Cita")
        self.citas.append(cita)

    def mostrar_info(self):
        return (
            f"Paciente [{self.id_paciente}] - {self.nombre} | "
            f"Edad: {self.edad} | DNI: {self.dni} | Seguro: {self.tiene_seguro}"
        )


class ServicioMedico:

    def __init__(self, id_servicio, nombre, coste):
        self.id_servicio = id_servicio
        self.nombre = nombre
        self.coste = coste

    @property
    def id_servicio(self):
        return self.__id_servicio

    @id_servicio.setter
    def id_servicio(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del servicio debe ser un entero positivo")
        self.__id_servicio = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del servicio no puede estar vacío")
        self.__nombre = valor.strip()

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El coste del servicio debe ser positivo")
        self.__coste = float(valor)

    def calcular_importe(self, paciente):
        raise NotImplementedError("Este método debe implementarse en las subclases")

    def mostrar_info(self):
        return f"Servicio [{self.id_servicio}] - {self.nombre} | Coste: {self.coste:.2f}€"


class ConsultaMedica(ServicioMedico):

    def __init__(self, id_servicio, nombre, coste, especialidad, es_urgente=False):
        super().__init__(id_servicio, nombre, coste)
        self.especialidad = especialidad
        self.es_urgente = es_urgente

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not isinstance(valor, Especialidad):
            raise TypeError("La especialidad debe ser un objeto de la clase Especialidad")
        self.__especialidad = valor

    @property
    def es_urgente(self):
        return self.__es_urgente

    @es_urgente.setter
    def es_urgente(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El campo es_urgente debe ser booleano")
        self.__es_urgente = valor

    def calcular_importe(self, paciente):
        importe = self.coste + self.especialidad.coste_base
        if self.es_urgente:
            importe *= 1.35
        if paciente.tiene_seguro:
            importe *= 0.60
        return importe

    def mostrar_info(self):
        return (
            super().mostrar_info()
            + f" | Tipo: Consulta | Especialidad: {self.especialidad.nombre} | Urgente: {self.es_urgente}"
        )


class PruebaDiagnostica(ServicioMedico):

    def __init__(self, id_servicio, nombre, coste, requiere_ayuno, complejidad):
        super().__init__(id_servicio, nombre, coste)
        self.requiere_ayuno = requiere_ayuno
        self.complejidad = complejidad

    @property
    def requiere_ayuno(self):
        return self.__requiere_ayuno

    @requiere_ayuno.setter
    def requiere_ayuno(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El campo requiere_ayuno debe ser booleano")
        self.__requiere_ayuno = valor

    @property
    def complejidad(self):
        return self.__complejidad

    @complejidad.setter
    def complejidad(self, valor):
        complejidades = ["baja", "media", "alta"]
        if not isinstance(valor, str) or valor.strip().lower() not in complejidades:
            raise ValueError("La complejidad debe ser baja, media o alta")
        self.__complejidad = valor.strip().lower()

    def calcular_importe(self, paciente):
        multiplicadores = {
            "baja": 1,
            "media": 1.25,
            "alta": 1.60
        }
        importe = self.coste * multiplicadores[self.complejidad]
        if paciente.tiene_seguro:
            importe *= 0.70
        return importe

    def mostrar_info(self):
        return (
            super().mostrar_info()
            + f" | Tipo: Prueba diagnóstica | Ayuno: {self.requiere_ayuno} | Complejidad: {self.complejidad}"
        )


class Tratamiento(ServicioMedico):

    def __init__(self, id_servicio, nombre, coste, numero_sesiones, descuento_por_paquete):
        super().__init__(id_servicio, nombre, coste)
        self.numero_sesiones = numero_sesiones
        self.descuento_por_paquete = descuento_por_paquete

    @property
    def numero_sesiones(self):
        return self.__numero_sesiones

    @numero_sesiones.setter
    def numero_sesiones(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El número de sesiones debe ser un entero positivo")
        self.__numero_sesiones = valor

    @property
    def descuento_por_paquete(self):
        return self.__descuento_por_paquete

    @descuento_por_paquete.setter
    def descuento_por_paquete(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 40:
            raise ValueError("El descuento debe estar entre 0 y 40")
        self.__descuento_por_paquete = float(valor)

    def calcular_importe(self, paciente):
        importe = self.coste * self.numero_sesiones
        importe *= 1 - self.descuento_por_paquete / 100
        if paciente.tiene_seguro:
            importe *= 0.80
        return importe

    def mostrar_info(self):
        return (
            super().mostrar_info()
            + f" | Tipo: Tratamiento | Sesiones: {self.numero_sesiones} | "
              f"Descuento paquete: {self.descuento_por_paquete:.2f}%"
        )


class Cita:

    ESTADOS_VALIDOS = ["programada", "realizada", "cancelada"]

    def __init__(self, id_cita, paciente, medico, servicio, fecha_hora):
        self.id_cita = id_cita
        self.paciente = paciente
        self.medico = medico
        self.servicio = servicio
        self.fecha_hora = fecha_hora
        self.estado = "programada"

    @property
    def id_cita(self):
        return self.__id_cita

    @id_cita.setter
    def id_cita(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID de la cita debe ser un entero positivo")
        self.__id_cita = valor

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise TypeError("El paciente debe ser un objeto de la clase Paciente")
        self.__paciente = valor

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, valor):
        if not isinstance(valor, Medico):
            raise TypeError("El médico debe ser un objeto de la clase Medico")
        self.__medico = valor

    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self, valor):
        if not isinstance(valor, ServicioMedico):
            raise TypeError("El servicio debe ser un objeto de la clase ServicioMedico")
        self.__servicio = valor

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @fecha_hora.setter
    def fecha_hora(self, valor):
        if not isinstance(valor, datetime):
            raise TypeError("La fecha y hora debe ser un objeto datetime")
        self.__fecha_hora = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, str) or valor.strip().lower() not in self.ESTADOS_VALIDOS:
            raise ValueError("El estado de la cita no es válido")
        self.__estado = valor.strip().lower()

    def realizar(self, diagnostico):
        if self.estado == "cancelada":
            raise ValueError("No se puede realizar una cita cancelada")
        if self.estado == "realizada":
            raise ValueError("La cita ya ha sido realizada")
        self.estado = "realizada"
        self.paciente.historial.agregar_registro(self, diagnostico)

    def cancelar(self):
        if self.estado == "realizada":
            raise ValueError("No se puede cancelar una cita ya realizada")
        self.estado = "cancelada"

    def calcular_importe(self):
        return self.servicio.calcular_importe(self.paciente)

    def mostrar_info(self):
        return (
            f"Cita [{self.id_cita}] | Paciente: {self.paciente.nombre} | "
            f"Médico: {self.medico.nombre} | Servicio: {self.servicio.nombre} | "
            f"Fecha: {self.fecha_hora.strftime('%d/%m/%Y %H:%M')} | "
            f"Estado: {self.estado} | Importe: {self.calcular_importe():.2f}€"
        )


class HistorialClinico:

    def __init__(self, paciente):
        self.paciente = paciente
        self.registros = []

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise TypeError("El paciente debe ser un objeto de la clase Paciente")
        self.__paciente = valor

    def agregar_registro(self, cita, diagnostico):
        if not isinstance(cita, Cita):
            raise TypeError("La cita debe ser un objeto de la clase Cita")
        if not isinstance(diagnostico, str) or not diagnostico.strip():
            raise ValueError("El diagnóstico no puede estar vacío")

        self.registros.append({
            "fecha": cita.fecha_hora,
            "medico": cita.medico.nombre,
            "servicio": cita.servicio.nombre,
            "diagnostico": diagnostico.strip()
        })

    def numero_registros(self):
        return len(self.registros)

    def mostrar_historial(self):
        if not self.registros:
            return f"El paciente {self.paciente.nombre} no tiene registros clínicos"

        texto = f"Historial clínico de {self.paciente.nombre}\n"
        for registro in self.registros:
            texto += (
                f"- {registro['fecha'].strftime('%d/%m/%Y %H:%M')} | "
                f"{registro['medico']} | {registro['servicio']} | "
                f"Diagnóstico: {registro['diagnostico']}\n"
            )
        return texto.strip()


class Factura:

    ESTADOS_VALIDOS = ["pendiente", "pagada", "anulada"]

    def __init__(self, id_factura, paciente, citas):
        self.id_factura = id_factura
        self.paciente = paciente
        self.citas = citas
        self.estado = "pendiente"

    @property
    def id_factura(self):
        return self.__id_factura

    @id_factura.setter
    def id_factura(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID de la factura debe ser un entero positivo")
        self.__id_factura = valor

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise TypeError("El paciente debe ser un objeto de la clase Paciente")
        self.__paciente = valor

    @property
    def citas(self):
        return self.__citas

    @citas.setter
    def citas(self, valor):
        if not isinstance(valor, list) or len(valor) == 0:
            raise ValueError("La factura debe contener al menos una cita")
        for cita in valor:
            if not isinstance(cita, Cita):
                raise TypeError("Todas las citas deben ser objetos de la clase Cita")
            if cita.paciente.id_paciente != self.paciente.id_paciente:
                raise ValueError("Todas las citas deben pertenecer al mismo paciente")
            if cita.estado != "realizada":
                raise ValueError("Solo se pueden facturar citas realizadas")
        self.__citas = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        if not isinstance(valor, str) or valor.strip().lower() not in self.ESTADOS_VALIDOS:
            raise ValueError("El estado de la factura no es válido")
        self.__estado = valor.strip().lower()

    def calcular_total(self):
        return sum(cita.calcular_importe() for cita in self.citas)

    def pagar(self):
        if self.estado == "anulada":
            raise ValueError("No se puede pagar una factura anulada")
        if self.estado == "pagada":
            raise ValueError("La factura ya está pagada")
        self.estado = "pagada"

    def anular(self):
        if self.estado == "pagada":
            raise ValueError("No se puede anular una factura pagada")
        self.estado = "anulada"

    def mostrar_info(self):
        return (
            f"Factura [{self.id_factura}] | Paciente: {self.paciente.nombre} | "
            f"Citas: {len(self.citas)} | Total: {self.calcular_total():.2f}€ | "
            f"Estado: {self.estado}"
        )


class Clinica:

    def __init__(self, nombre):
        self.nombre = nombre
        self.especialidades = []
        self.medicos = []
        self.pacientes = []
        self.servicios = []
        self.citas = []
        self.facturas = []

    def agregar_especialidad(self, especialidad):
        if not isinstance(especialidad, Especialidad):
            raise TypeError("Solo se pueden agregar objetos de tipo Especialidad")
        for esp in self.especialidades:
            if esp.id_especialidad == especialidad.id_especialidad:
                raise ValueError("Ya existe una especialidad con ese ID")
        self.especialidades.append(especialidad)

    def agregar_medico(self, medico):
        if not isinstance(medico, Medico):
            raise TypeError("Solo se pueden agregar objetos de tipo Medico")
        for med in self.medicos:
            if med.id_medico == medico.id_medico:
                raise ValueError("Ya existe un médico con ese ID")
            if med.numero_colegiado == medico.numero_colegiado:
                raise ValueError("Ya existe un médico con ese número de colegiado")

        especialidad_registrada = any(
            esp.id_especialidad == medico.especialidad.id_especialidad
            for esp in self.especialidades
        )

        if not especialidad_registrada:
            raise ValueError("La especialidad del médico no está registrada")

        self.medicos.append(medico)

    def agregar_paciente(self, paciente):
        if not isinstance(paciente, Paciente):
            raise TypeError("Solo se pueden agregar objetos de tipo Paciente")
        for pac in self.pacientes:
            if pac.id_paciente == paciente.id_paciente:
                raise ValueError("Ya existe un paciente con ese ID")
            if pac.dni == paciente.dni:
                raise ValueError("Ya existe un paciente con ese DNI")
        self.pacientes.append(paciente)

    def agregar_servicio(self, servicio):
        if not isinstance(servicio, ServicioMedico):
            raise TypeError("Solo se pueden agregar objetos de tipo ServicioMedico")
        for serv in self.servicios:
            if serv.id_servicio == servicio.id_servicio:
                raise ValueError("Ya existe un servicio con ese ID")
        self.servicios.append(servicio)

    def programar_cita(self, id_cita, paciente, medico, servicio, fecha_hora):
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser un objeto de la clase Paciente")
        if not isinstance(medico, Medico):
            raise TypeError("El médico debe ser un objeto de la clase Medico")
        if not isinstance(servicio, ServicioMedico):
            raise TypeError("El servicio debe ser un objeto de la clase ServicioMedico")

        if not medico.activo:
            raise ValueError("No se puede programar una cita con un médico inactivo")

        for cita in self.citas:
            if cita.id_cita == id_cita:
                raise ValueError("Ya existe una cita con ese ID")

        paciente_registrado = any(p.id_paciente == paciente.id_paciente for p in self.pacientes)
        medico_registrado = any(m.id_medico == medico.id_medico for m in self.medicos)
        servicio_registrado = any(s.id_servicio == servicio.id_servicio for s in self.servicios)

        if not paciente_registrado:
            raise ValueError("El paciente no está registrado en la clínica")
        if not medico_registrado:
            raise ValueError("El médico no está registrado en la clínica")
        if not servicio_registrado:
            raise ValueError("El servicio no está registrado en la clínica")
        if medico.tiene_cita_en_fecha(fecha_hora):
            raise ValueError("El médico ya tiene una cita programada en esa fecha y hora")

        cita = Cita(id_cita, paciente, medico, servicio, fecha_hora)
        self.citas.append(cita)
        paciente.agregar_cita(cita)
        medico.agregar_cita(cita)
        return cita

    def generar_factura(self, id_factura, paciente, citas):
        for factura in self.facturas:
            if factura.id_factura == id_factura:
                raise ValueError("Ya existe una factura con ese ID")

        factura = Factura(id_factura, paciente, citas)
        self.facturas.append(factura)
        return factura

    def ingresos_totales(self):
        return sum(
            factura.calcular_total()
            for factura in self.facturas
            if factura.estado == "pagada"
        )

    def citas_por_paciente(self, id_paciente):
        if not isinstance(id_paciente, int) or id_paciente <= 0:
            raise ValueError("El ID del paciente debe ser un entero positivo")
        return [
            cita for cita in self.citas
            if cita.paciente.id_paciente == id_paciente
        ]

    def citas_por_medico(self, id_medico):
        if not isinstance(id_medico, int) or id_medico <= 0:
            raise ValueError("El ID del médico debe ser un entero positivo")
        return [
            cita for cita in self.citas
            if cita.medico.id_medico == id_medico
        ]

    def servicios_mas_caros_que(self, precio, paciente):
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser mayor o igual que cero")
        if not isinstance(paciente, Paciente):
            raise TypeError("El paciente debe ser un objeto de la clase Paciente")
        return [
            servicio for servicio in self.servicios
            if servicio.calcular_importe(paciente) > precio
        ]

    def mostrar_resumen(self):
        return (
            f"Clínica: {self.nombre} | "
            f"Especialidades: {len(self.especialidades)} | "
            f"Médicos: {len(self.medicos)} | "
            f"Pacientes: {len(self.pacientes)} | "
            f"Servicios: {len(self.servicios)} | "
            f"Citas: {len(self.citas)} | "
            f"Facturas: {len(self.facturas)} | "
            f"Ingresos pagados: {self.ingresos_totales():.2f}€"
        )


def probar_error(descripcion, funcion):
    try:
        funcion()
    except Exception as error:
        print(f"{descripcion}: {error}")


def main():
    clinica = Clinica("Clínica Python Salud")

    cardiologia = Especialidad(1, "Cardiología", 60)
    traumatologia = Especialidad(2, "Traumatología", 50)
    neurologia = Especialidad(3, "Neurología", 80)

    clinica.agregar_especialidad(cardiologia)
    clinica.agregar_especialidad(traumatologia)
    clinica.agregar_especialidad(neurologia)

    medico1 = Medico(1, "Laura Gómez", cardiologia, "COL123")
    medico2 = Medico(2, "Carlos Ruiz", traumatologia, "COL456")
    medico3 = Medico(3, "Marta López", neurologia, "COL789", activo=False)

    clinica.agregar_medico(medico1)
    clinica.agregar_medico(medico2)
    clinica.agregar_medico(medico3)

    paciente1 = Paciente(1, "Ana Torres", 34, "12345678A", tiene_seguro=True)
    paciente2 = Paciente(2, "Pedro Martín", 52, "87654321B", tiene_seguro=False)

    clinica.agregar_paciente(paciente1)
    clinica.agregar_paciente(paciente2)

    consulta_cardiologia = ConsultaMedica(1, "Consulta cardiológica", 45, cardiologia, es_urgente=False)
    consulta_urgente = ConsultaMedica(2, "Consulta urgente traumatología", 50, traumatologia, es_urgente=True)
    resonancia = PruebaDiagnostica(3, "Resonancia magnética", 220, requiere_ayuno=False, complejidad="alta")
    rehabilitacion = Tratamiento(4, "Rehabilitación funcional", 35, numero_sesiones=10, descuento_por_paquete=15)

    clinica.agregar_servicio(consulta_cardiologia)
    clinica.agregar_servicio(consulta_urgente)
    clinica.agregar_servicio(resonancia)
    clinica.agregar_servicio(rehabilitacion)

    cita1 = clinica.programar_cita(
        1,
        paciente1,
        medico1,
        consulta_cardiologia,
        datetime(2026, 5, 4, 10, 0)
    )

    cita2 = clinica.programar_cita(
        2,
        paciente1,
        medico2,
        resonancia,
        datetime(2026, 5, 5, 12, 30)
    )

    cita3 = clinica.programar_cita(
        3,
        paciente2,
        medico2,
        rehabilitacion,
        datetime(2026, 5, 6, 9, 0)
    )

    print("=== RESUMEN INICIAL ===")
    print(clinica.mostrar_resumen())

    print("\n=== INFORMACIÓN DE ESPECIALIDADES ===")
    for especialidad in clinica.especialidades:
        print(especialidad.mostrar_info())

    print("\n=== INFORMACIÓN DE MÉDICOS ===")
    for medico in clinica.medicos:
        print(medico.mostrar_info())

    print("\n=== INFORMACIÓN DE PACIENTES ===")
    for paciente in clinica.pacientes:
        print(paciente.mostrar_info())

    print("\n=== INFORMACIÓN DE SERVICIOS ===")
    for servicio in clinica.servicios:
        print(servicio.mostrar_info())

    print("\n=== CITAS PROGRAMADAS ===")
    for cita in clinica.citas:
        print(cita.mostrar_info())

    cita1.realizar("Revisión cardiológica sin alteraciones relevantes")
    cita2.realizar("Se recomienda valoración médica tras resultados de imagen")
    cita3.realizar("Inicio de tratamiento de rehabilitación por lesión muscular")

    print("\n=== CITAS TRAS SER REALIZADAS ===")
    for cita in clinica.citas:
        print(cita.mostrar_info())

    factura1 = clinica.generar_factura(1, paciente1, [cita1, cita2])
    factura2 = clinica.generar_factura(2, paciente2, [cita3])

    print("\n=== FACTURAS GENERADAS ===")
    print(factura1.mostrar_info())
    print(factura2.mostrar_info())

    factura1.pagar()
    factura2.pagar()

    print("\n=== FACTURAS PAGADAS ===")
    print(factura1.mostrar_info())
    print(factura2.mostrar_info())

    print("\n=== HISTORIALES CLÍNICOS ===")
    print(paciente1.historial.mostrar_historial())
    print()
    print(paciente2.historial.mostrar_historial())

    print("\n=== CITAS POR PACIENTE ===")
    for cita in clinica.citas_por_paciente(1):
        print(cita.mostrar_info())

    print("\n=== CITAS POR MÉDICO ===")
    for cita in clinica.citas_por_medico(2):
        print(cita.mostrar_info())

    print("\n=== SERVICIOS DE MÁS DE 100€ PARA PACIENTE SIN SEGURO ===")
    for servicio in clinica.servicios_mas_caros_que(100, paciente2):
        print(servicio.mostrar_info())

    print("\n=== RESUMEN FINAL ===")
    print(clinica.mostrar_resumen())

    print("\n=== PRUEBAS DE ERRORES CONTROLADOS ===")

    probar_error(
        "Error por especialidad duplicada",
        lambda: clinica.agregar_especialidad(Especialidad(1, "Dermatología", 40))
    )

    probar_error(
        "Error por médico duplicado",
        lambda: clinica.agregar_medico(Medico(4, "Juan Pérez", cardiologia, "COL123"))
    )

    probar_error(
        "Error por paciente duplicado",
        lambda: clinica.agregar_paciente(Paciente(3, "Luis Cano", 45, "12345678A"))
    )

    probar_error(
        "Error por médico inactivo",
        lambda: clinica.programar_cita(
            4,
            paciente1,
            medico3,
            consulta_cardiologia,
            datetime(2026, 5, 7, 11, 0)
        )
    )

    probar_error(
        "Error por cita duplicada en la agenda del médico",
        lambda: clinica.programar_cita(
            5,
            paciente2,
            medico1,
            consulta_cardiologia,
            datetime(2026, 5, 4, 10, 0)
        )
    )

    probar_error(
        "Error por cancelar cita realizada",
        lambda: cita1.cancelar()
    )

    probar_error(
        "Error por facturar cita no realizada",
        lambda: clinica.generar_factura(
            3,
            paciente1,
            [
                clinica.programar_cita(
                    6,
                    paciente1,
                    medico1,
                    consulta_cardiologia,
                    datetime(2026, 5, 8, 10, 0)
                )
            ]
        )
    )

    probar_error(
        "Error por servicio con complejidad incorrecta",
        lambda: PruebaDiagnostica(10, "Prueba inválida", 100, False, "extrema")
    )

    probar_error(
        "Error por tratamiento con descuento incorrecto",
        lambda: Tratamiento(11, "Tratamiento inválido", 40, 5, 80)
    )


if __name__ == "__main__":
    main()