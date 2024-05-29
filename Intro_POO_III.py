class Empleado:
    def pedir_nombre(self):
        self.nombre = str(input("Ingrese el nombre del empleado: "))

class Salario:
    def pedir_salario(self):
        self.salario = float(input("Ingrese el salario del empleado: "))

class Designacion(Empleado, Salario):
    def designar_cargo(self, cargo):
        self.cargo = cargo

# Verificar el código
empleado_designado = Designacion()

# Pedir nombre y salario
empleado_designado.pedir_nombre()
empleado_designado.pedir_salario()

# Verificar si el objeto tiene los métodos nombre y salario
tiene_metodo_nombre = hasattr(empleado_designado, 'nombre')
tiene_metodo_salario = hasattr(empleado_designado, 'salario')

print("El objeto tiene el método 'nombre':", tiene_metodo_nombre)
print("El objeto tiene el método 'salario':", tiene_metodo_salario)