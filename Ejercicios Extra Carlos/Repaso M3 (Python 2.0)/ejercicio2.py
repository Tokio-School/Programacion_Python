class Profesor:

    def __init__(self, id_profesor, nombre, especialidad, valoracion):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.especialidad = especialidad
        self.valoracion = valoracion

    @property
    def id_profesor(self):
        return self.__id_profesor

    @id_profesor.setter
    def id_profesor(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del profesor debe ser un entero positivo")
        self.__id_profesor = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del profesor no puede estar vacío")
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError("El nombre del profesor debe tener al menos 3 caracteres")
        self.__nombre = valor

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La especialidad no puede estar vacía")
        self.__especialidad = valor.strip()

    @property
    def valoracion(self):
        return self.__valoracion

    @valoracion.setter
    def valoracion(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 5:
            raise ValueError("La valoración debe estar entre 0 y 5")
        self.__valoracion = float(valor)

    def mostrar_info(self):
        return (
            f"Profesor [{self.id_profesor}] - {self.nombre} | "
            f"Especialidad: {self.especialidad} | Valoración: {self.valoracion:.1f}/5"
        )


class Curso:

    def __init__(self, id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima):
        self.id_curso = id_curso
        self.titulo = titulo
        self.profesor = profesor
        self.precio_base = precio_base
        self.duracion_horas = duracion_horas
        self.nivel = nivel
        self.capacidad_maxima = capacidad_maxima
        self.matriculas = []

    @property
    def id_curso(self):
        return self.__id_curso

    @id_curso.setter
    def id_curso(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del curso debe ser un entero positivo")
        self.__id_curso = valor

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El título del curso no puede estar vacío")
        valor = valor.strip()
        if len(valor) < 5:
            raise ValueError("El título del curso debe tener al menos 5 caracteres")
        self.__titulo = valor

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, valor):
        if not isinstance(valor, Profesor):
            raise TypeError("El profesor debe ser un objeto de la clase Profesor")
        self.__profesor = valor

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio base debe ser un número positivo")
        self.__precio_base = float(valor)

    @property
    def duracion_horas(self):
        return self.__duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La duración debe ser un número positivo")
        self.__duracion_horas = float(valor)

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, valor):
        niveles_validos = ["básico", "intermedio", "avanzado"]
        if not isinstance(valor, str) or valor.strip().lower() not in niveles_validos:
            raise ValueError("El nivel debe ser básico, intermedio o avanzado")
        self.__nivel = valor.strip().lower()

    @property
    def capacidad_maxima(self):
        return self.__capacidad_maxima

    @capacidad_maxima.setter
    def capacidad_maxima(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La capacidad máxima debe ser un entero positivo")
        self.__capacidad_maxima = valor

    def plazas_disponibles(self):
        return self.capacidad_maxima - len(self.matriculas)

    def esta_completo(self):
        return self.plazas_disponibles() == 0

    def agregar_matricula(self, matricula):
        if not isinstance(matricula, Matricula):
            raise TypeError("Solo se pueden agregar objetos de tipo Matricula")
        if self.esta_completo():
            raise ValueError("El curso no tiene plazas disponibles")
        self.matriculas.append(matricula)

    def calcular_precio_final(self):
        raise NotImplementedError("Este método debe implementarse en las subclases")

    def mostrar_info(self):
        return (
            f"Curso [{self.id_curso}] - {self.titulo} | "
            f"Profesor: {self.profesor.nombre} | Nivel: {self.nivel} | "
            f"Duración: {self.duracion_horas:.1f} horas | "
            f"Precio final: {self.calcular_precio_final():.2f}€ | "
            f"Plazas disponibles: {self.plazas_disponibles()}"
        )


class CursoGrabado(Curso):

    def __init__(self, id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima, meses_acceso):
        super().__init__(id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima)
        self.meses_acceso = meses_acceso

    @property
    def meses_acceso(self):
        return self.__meses_acceso

    @meses_acceso.setter
    def meses_acceso(self, valor):
        if not isinstance(valor, int) or valor <= 0 or valor > 36:
            raise ValueError("Los meses de acceso deben estar entre 1 y 36")
        self.__meses_acceso = valor

    def calcular_precio_final(self):
        incremento = 0
        if self.meses_acceso > 12:
            incremento = self.precio_base * 0.10
        return self.precio_base + incremento

    def mostrar_info(self):
        return (
            super().mostrar_info()
            + f" | Tipo: Grabado | Meses de acceso: {self.meses_acceso}"
        )


class CursoEnDirecto(Curso):

    def __init__(self, id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima, numero_sesiones, incluye_tutoria):
        super().__init__(id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima)
        self.numero_sesiones = numero_sesiones
        self.incluye_tutoria = incluye_tutoria

    @property
    def numero_sesiones(self):
        return self.__numero_sesiones

    @numero_sesiones.setter
    def numero_sesiones(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El número de sesiones debe ser un entero positivo")
        self.__numero_sesiones = valor

    @property
    def incluye_tutoria(self):
        return self.__incluye_tutoria

    @incluye_tutoria.setter
    def incluye_tutoria(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El campo incluye_tutoria debe ser booleano")
        self.__incluye_tutoria = valor

    def calcular_precio_final(self):
        precio = self.precio_base + self.numero_sesiones * 15
        if self.incluye_tutoria:
            precio += 80
        return precio

    def mostrar_info(self):
        return (
            super().mostrar_info()
            + f" | Tipo: En directo | Sesiones: {self.numero_sesiones} | "
              f"Tutoría incluida: {self.incluye_tutoria}"
        )


class CursoCertificado(Curso):

    def __init__(self, id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima, coste_certificacion, examen_final):
        super().__init__(id_curso, titulo, profesor, precio_base, duracion_horas, nivel, capacidad_maxima)
        self.coste_certificacion = coste_certificacion
        self.examen_final = examen_final

    @property
    def coste_certificacion(self):
        return self.__coste_certificacion

    @coste_certificacion.setter
    def coste_certificacion(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El coste de certificación debe ser mayor o igual que cero")
        self.__coste_certificacion = float(valor)

    @property
    def examen_final(self):
        return self.__examen_final

    @examen_final.setter
    def examen_final(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El campo examen_final debe ser booleano")
        self.__examen_final = valor

    def calcular_precio_final(self):
        precio = self.precio_base + self.coste_certificacion
        if self.examen_final:
            precio += 50
        if self.nivel == "avanzado":
            precio *= 1.15
        return precio

    def mostrar_info(self):
        return (
            super().mostrar_info()
            + f" | Tipo: Certificado | Coste certificación: {self.coste_certificacion:.2f}€ | "
              f"Examen final: {self.examen_final}"
        )


class Estudiante:

    def __init__(self, id_estudiante, nombre, email, edad):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.matriculas = []

    @property
    def id_estudiante(self):
        return self.__id_estudiante

    @id_estudiante.setter
    def id_estudiante(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del estudiante debe ser un entero positivo")
        self.__id_estudiante = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del estudiante no puede estar vacío")
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError("El nombre del estudiante debe tener al menos 3 caracteres")
        self.__nombre = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise ValueError("El email no tiene un formato válido")
        self.__email = valor.strip().lower()

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or valor < 14:
            raise ValueError("La edad del estudiante debe ser un entero mayor o igual que 14")
        self.__edad = valor

    def agregar_matricula(self, matricula):
        if not isinstance(matricula, Matricula):
            raise TypeError("Solo se pueden agregar objetos de tipo Matricula")
        self.matriculas.append(matricula)

    def cursos_activos(self):
        return [
            matricula.curso for matricula in self.matriculas
            if not matricula.completado
        ]

    def gasto_total_formacion(self):
        return sum(matricula.precio_pagado for matricula in self.matriculas)

    def mostrar_info(self):
        return (
            f"Estudiante [{self.id_estudiante}] - {self.nombre} | "
            f"Email: {self.email} | Edad: {self.edad} | "
            f"Matrículas: {len(self.matriculas)}"
        )


class Matricula:

    def __init__(self, estudiante, curso, actividades_totales, descuento):
        self.estudiante = estudiante
        self.curso = curso
        self.actividades_totales = actividades_totales
        self.actividades_completadas = 0
        self.descuento = descuento
        self.precio_pagado = self.calcular_precio_pagado()
        self.completado = False

    @property
    def estudiante(self):
        return self.__estudiante

    @estudiante.setter
    def estudiante(self, valor):
        if not isinstance(valor, Estudiante):
            raise TypeError("El estudiante debe ser un objeto de la clase Estudiante")
        self.__estudiante = valor

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, valor):
        if not isinstance(valor, Curso):
            raise TypeError("El curso debe ser un objeto de la clase Curso")
        self.__curso = valor

    @property
    def actividades_totales(self):
        return self.__actividades_totales

    @actividades_totales.setter
    def actividades_totales(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Las actividades totales deben ser un entero positivo")
        self.__actividades_totales = valor

    @property
    def actividades_completadas(self):
        return self.__actividades_completadas

    @actividades_completadas.setter
    def actividades_completadas(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Las actividades completadas deben ser un entero mayor o igual que cero")
        if hasattr(self, "_Matricula__actividades_totales") and valor > self.actividades_totales:
            raise ValueError("Las actividades completadas no pueden superar las actividades totales")
        self.__actividades_completadas = valor

    @property
    def descuento(self):
        return self.__descuento

    @descuento.setter
    def descuento(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 50:
            raise ValueError("El descuento debe estar entre 0 y 50")
        self.__descuento = float(valor)

    @property
    def precio_pagado(self):
        return self.__precio_pagado

    @precio_pagado.setter
    def precio_pagado(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El precio pagado debe ser mayor o igual que cero")
        self.__precio_pagado = float(valor)

    @property
    def completado(self):
        return self.__completado

    @completado.setter
    def completado(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El campo completado debe ser booleano")
        self.__completado = valor

    def calcular_precio_pagado(self):
        return self.curso.calcular_precio_final() * (1 - self.descuento / 100)

    def completar_actividades(self, cantidad):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad de actividades debe ser un entero positivo")
        self.actividades_completadas = min(
            self.actividades_completadas + cantidad,
            self.actividades_totales
        )
        if self.actividades_completadas == self.actividades_totales:
            self.completado = True

    def calcular_progreso(self):
        return self.actividades_completadas / self.actividades_totales * 100

    def mostrar_info(self):
        return (
            f"Estudiante: {self.estudiante.nombre} | "
            f"Curso: {self.curso.titulo} | "
            f"Precio pagado: {self.precio_pagado:.2f}€ | "
            f"Progreso: {self.calcular_progreso():.2f}% | "
            f"Completado: {self.completado}"
        )


class Plataforma:

    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = []
        self.estudiantes = []
        self.cursos = []
        self.matriculas = []

    def agregar_profesor(self, profesor):
        if not isinstance(profesor, Profesor):
            raise TypeError("Solo se pueden agregar objetos de tipo Profesor")
        for prof in self.profesores:
            if prof.id_profesor == profesor.id_profesor:
                raise ValueError("Ya existe un profesor con ese ID")
        self.profesores.append(profesor)

    def agregar_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise TypeError("Solo se pueden agregar objetos de tipo Estudiante")
        for est in self.estudiantes:
            if est.id_estudiante == estudiante.id_estudiante:
                raise ValueError("Ya existe un estudiante con ese ID")
            if est.email == estudiante.email:
                raise ValueError("Ya existe un estudiante con ese email")
        self.estudiantes.append(estudiante)

    def agregar_curso(self, curso):
        if not isinstance(curso, Curso):
            raise TypeError("Solo se pueden agregar objetos de tipo Curso o subclases")
        for cur in self.cursos:
            if cur.id_curso == curso.id_curso:
                raise ValueError("Ya existe un curso con ese ID")
        profesor_registrado = any(
            profesor.id_profesor == curso.profesor.id_profesor
            for profesor in self.profesores
        )
        if not profesor_registrado:
            raise ValueError("No se puede agregar el curso porque el profesor no está registrado")
        self.cursos.append(curso)

    def matricular_estudiante(self, estudiante, curso, actividades_totales, descuento=0):
        if not isinstance(estudiante, Estudiante):
            raise TypeError("El estudiante debe ser un objeto de la clase Estudiante")
        if not isinstance(curso, Curso):
            raise TypeError("El curso debe ser un objeto de la clase Curso")

        estudiante_registrado = any(
            est.id_estudiante == estudiante.id_estudiante
            for est in self.estudiantes
        )

        curso_registrado = any(
            cur.id_curso == curso.id_curso
            for cur in self.cursos
        )

        if not estudiante_registrado:
            raise ValueError("El estudiante no está registrado en la plataforma")

        if not curso_registrado:
            raise ValueError("El curso no está registrado en la plataforma")

        for matricula in self.matriculas:
            if (
                matricula.estudiante.id_estudiante == estudiante.id_estudiante
                and matricula.curso.id_curso == curso.id_curso
            ):
                raise ValueError("El estudiante ya está matriculado en este curso")

        if curso.esta_completo():
            raise ValueError("El curso está completo")

        matricula = Matricula(estudiante, curso, actividades_totales, descuento)
        self.matriculas.append(matricula)
        estudiante.agregar_matricula(matricula)
        curso.agregar_matricula(matricula)
        return matricula

    def ingresos_totales(self):
        return sum(matricula.precio_pagado for matricula in self.matriculas)

    def cursos_por_profesor(self, id_profesor):
        if not isinstance(id_profesor, int) or id_profesor <= 0:
            raise ValueError("El ID del profesor debe ser un entero positivo")
        return [
            curso for curso in self.cursos
            if curso.profesor.id_profesor == id_profesor
        ]

    def estudiantes_por_curso(self, id_curso):
        if not isinstance(id_curso, int) or id_curso <= 0:
            raise ValueError("El ID del curso debe ser un entero positivo")
        return [
            matricula.estudiante for matricula in self.matriculas
            if matricula.curso.id_curso == id_curso
        ]

    def cursos_mas_caros_que(self, precio):
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser mayor o igual que cero")
        return [
            curso for curso in self.cursos
            if curso.calcular_precio_final() > precio
        ]

    def promedio_progreso_estudiantes(self):
        if len(self.matriculas) == 0:
            return 0
        return sum(matricula.calcular_progreso() for matricula in self.matriculas) / len(self.matriculas)

    def mostrar_resumen(self):
        return (
            f"Plataforma: {self.nombre} | "
            f"Profesores: {len(self.profesores)} | "
            f"Estudiantes: {len(self.estudiantes)} | "
            f"Cursos: {len(self.cursos)} | "
            f"Matrículas: {len(self.matriculas)} | "
            f"Ingresos totales: {self.ingresos_totales():.2f}€"
        )