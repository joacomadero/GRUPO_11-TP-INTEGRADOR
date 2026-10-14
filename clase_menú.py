import Producto
class Menu:
    def __init__ (self, menu):
        self.menu = menu

    def info (self):
        print("--------------------------------------")
        print("          LA COMANDA - MENÚ")
        for seccion, contenido in self.menu.items():
            print("--------------------------------------")
            print(f"{seccion}")
            print("--------------------------------------")
            for elemento, precio in contenido.items():
                print(f"{elemento:<{29}} - ${precio}")
        print("--------------------------------------")


comida_1 = Producto.Comida("Milanesa", 10000, False)
comida_2 = Producto.Comida("Pastas", 9000, True)
comida_3 = Producto.Comida("Empanadas", 11000, False)

bebida_1 = Producto.Bebida("Coca-Cola", 5000, "1.5 L")
bebida_2 = Producto.Bebida("Sprite", 5000, "1.5 L")
bebida_3 = Producto.Bebida("Agua Mineral", 3500, "500 mL")

carta = {
    "Comidas": {comida_1.nombre: comida_1.precio,
                comida_2.nombre: comida_2.precio,
                comida_3.nombre: comida_3.precio},

    "Bebidas": {bebida_1.nombre: bebida_1.precio,
                bebida_2.nombre: bebida_2.precio,
                bebida_3.nombre: bebida_3.precio,}
}

MENÚ_FINAL = Menu(carta)

def mostrar_menu():
    MENÚ_FINAL.info()
        
   
    
   
        
    
        

        
    
        
    
        