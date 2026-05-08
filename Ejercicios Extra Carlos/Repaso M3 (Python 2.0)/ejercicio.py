class Departamento:

    def __init__(self, id_departamento, nombre, presupuesto):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.presupuesto_anual = presupuesto

    @property
    def id_departamento(self):
        return self.__id_departamento
    
    @id_departamento.setter
    def id_departamento(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del departamento debe ser un entero positivo")
        self.__id_departamento = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del empleado no puede estar vacio")
        self.__nombre = valor.strip()

    @property
    def presupuesto_anual(self):
        return self.__presupuesto_anual
    
    @presupuesto_anual.setter
    def presupuesto_anual(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El presupuesto anual debe ser un numero positivo")
        self.__presupuesto_anual = float(valor)

    def presupuesto_mensual(self):
        return self.presupuesto_anual / 12
    
    def puede_asumir_gasto(self, gasto_mensual):
        if not isinstance(gasto_mensual, (int, float)) or gasto_mensual < 0:
            raise ValueError("El gasto mensual debe ser un numero mayor o igual a cero")
        return gasto_mensual <= self.presupuesto_mensual()
    
    def mostrar_info(self):
        return (
            f"Departamento [{self.id_departamento}] - {self.nombre} | "
            f"Presupuesto anual: {self.presupuesto_anual:.2f}€ | "
            f"Presupuesto mensual: {self.presupuesto_mensual():.2f}€"
        )


class Empleado:

    def __init__(self, id_empleado, nombre, edad, departamento):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento

    @property
    def id_empleado(self):
        return self.__id_empleado
    
    @id_empleado.setter
    def id_empleado(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ID del empleado debe ser un entero positivo")
        self.__id_empleado = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del empleado no puede estar vacio")
        valor = valor.strip()
        if len(valor) < 3:
            raise ValueError("El nombre del empleado debe tener al menos 3 caracteres")
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int):
            raise ValueError("La edad del empleado debe ser un numero entero")
        if valor < 18 or valor > 67:
            raise ValueError("La edad del empleado debe estar entre 18 y 67 años")
        self.__edad = valor
    
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, valor):
        if not isinstance(valor, Departamento):
            raise TypeError("El departamento debe ser un objeto de la clase Departamento")
        self.__departamento = valor

    def calcular_salario(self):
        raise NotImplementedError("Este metodo debe implementarse en las subclases")
    
    def es_mayor_que(self, edad_limite):
        if not isinstance(edad_limite, int):
            raise ValueError("La edad limite debe ser un entero")
        return self.edad > edad_limite
    
    def mostrar_datos(self):
        return (
            f"ID: {self.id_empleado} | Nombre: {self.nombre} | Edad: {self.edad} | "
            f"Departamento: {self.departamento.nombre}"
        )
    

class EmpleadoFijo(Empleado):

    def __init__(self, id_empleado, nombre, edad, departamento, salario_base):
        super().__init__(id_empleado, nombre, edad, departamento)
        self.salario_base = salario_base

    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 1000:
            raise ValueError("El salario base debe ser un numero mayor que 1000")
        self.__salario_base = float(valor)

    def calcular_salario(self):
        return self.salario_base
    
    def mostrar_datos(self):
        return (
            super().mostrar_datos()
            + f" | Tipo: Fijo | Salario base: {self.salario_base:.2f}€"
        )
    

class EmpleadoPorHoras(Empleado):
    def __init__(self, id_empleado, nombre, edad, departamento, horas_trabajadas, precio_hora):
        super().__init__(id_empleado, nombre, edad, departamento)
        self.horas_trabajadas = horas_trabajadas
        self.precio_hora = precio_hora

    @property
    def horas_trabajadas(self):
        return self.__horas_trabajadas

    @horas_trabajadas.setter
    def horas_trabajadas(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Las horas trabajadas deben ser numéricas.")
        if valor < 0 or valor > 300:
            raise ValueError("Las horas trabajadas deben estar entre 0 y 300.")
        self.__horas_trabajadas = float(valor)

    @property
    def precio_hora(self):
        return self.__precio_hora

    @precio_hora.setter
    def precio_hora(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio por hora debe ser un número positivo.")
        self.__precio_hora = float(valor)

    def calcular_salario(self):
        horas_normales = min(self.horas_trabajadas, 160)
        horas_extra = max(self.horas_trabajadas - 160, 0)
        return (horas_normales * self.precio_hora) + (horas_extra * self.precio_hora * 1.5)

    def mostrar_datos(self):
        return (
            super().mostrar_datos()
            + f" | Tipo: Por horas | Horas trabajadas: {self.horas_trabajadas} | "
              f"Precio hora: {self.precio_hora:.2f} €"
        )
    

class EmpleadoComision(Empleado):
    def __init__(self, id_empleado, nombre, edad, departamento, salario_base, ventas, porcentaje_comision):
        super().__init__(id_empleado, nombre, edad, departamento)
        self.salario_base = salario_base
        self.ventas = ventas
        self.porcentaje_comision = porcentaje_comision

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if not isinstance(valor, (int, float)) or valor < 900:
            raise ValueError("El salario base debe ser un número mayor o igual que 900.")
        self.__salario_base = float(valor)

    @property
    def ventas(self):
        return self.__ventas

    @ventas.setter
    def ventas(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("Las ventas deben ser un número mayor o igual que 0.")
        self.__ventas = float(valor)

    @property
    def porcentaje_comision(self):
        return self.__porcentaje_comision

    @porcentaje_comision.setter
    def porcentaje_comision(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0 or valor > 20:
            raise ValueError("El porcentaje de comisión debe estar entre 0 y 20.")
        self.__porcentaje_comision = float(valor)

    def calcular_salario(self):
        salario = self.salario_base + (self.ventas * self.porcentaje_comision / 100)
        if self.ventas > 20000:
            salario += 300
        return salario

    def mostrar_datos(self):
        return (
            super().mostrar_datos()
            + f" | Tipo: Comisión | Base: {self.salario_base:.2f} € | "
              f"Ventas: {self.ventas:.2f} € | Comisión: {self.porcentaje_comision:.2f}%"
        )
    

class Empresa:

    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.departamentos = []

    def agregar_departamento(self, departamento):
        if not isinstance(departamento, Departamento):
            raise TypeError("Solo se pueden agregar objetos de tipo Departamento")
        
        for dep in self.departamentos:
            if dep.id_departamento == departamento.id_departamento:
                raise ValueError(f"Ya existe un departamento en la empresa con ID: {departamento.id_departamento}")
            
        self.departamentos.append(departamento)

    def agregar_empleado(self, empleado):
        if not isinstance(empleado, Empleado):
            raise TypeError("Solo se pueden agregar objetos de tipo Empleado o subclases")
        
        for emp in self.empleados:
            if emp.id_empleado == empleado.id_empleado:
                raise ValueError(f"Ya existe un empleado en la empresa con ID: {empleado.id_empleado}")
            
        departamento_existente = any(
            dep.id_departamento == empleado.departamento.id_departamento
            for dep in self.departamentos
        )

        if not departamento_existente:
            raise ValueError(
                f"No se puede agregar al empleado porque el departamento "
                f"{empleado.departamento.nombre} no esta registrado en la empresa"
            )
        
        self.empleados.append(empleado)

    def gasto_total_nominas(self):
        return sum(empleado.calcular_salario() for empleado in self.empleados)

    def empleados_por_departamento(self, nombre_departamento):
        if not isinstance(nombre_departamento, str) or not nombre_departamento.strip():
            raise ValueError("El nombre del departamento no puede estar vacio")
        
        nombre_departamento = nombre_departamento.strip().lower()

        return [
            empleado for empleado in self.empleados
            if empleado.departamento.nombre.lower() == nombre_departamento
        ]