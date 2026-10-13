

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def info(self):
        print(self.nombre, "- $", self.precio)


class Comida(Producto):
    def __init__(self, nombre, precio, celiaco=False):
        super().__init__(nombre, precio)
        self.celiaco = celiaco

    def info(self):
        super().info()
        if self.celiaco:
            print("Apta para celíacos")
        else:
            print("No apta para celíacos")


class Bebida(Producto):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def info(self):
        super().info()
        print("Tamaño:", self.tamaño)