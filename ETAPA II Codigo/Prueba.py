class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def __repr__(self):
        return f"Producto: {self.nombre}, Stock: {self.stock}"

def menu_principal(inventario):
    while True:
        print("\nMenu Principal:")
        print("a. Ver todos los productos")
        print("b. Ver productos con bajo stock")
        print("c. Agregar un producto")
        print("d. Eliminar un producto")
        print("e. Editar un producto")
        print("f. Salir")

        eleccion = input("Seleccione una opción: ")
        
        if eleccion == "a":
            inventario.mostrar_productos()
        elif eleccion == "b":
            menu_bajo_stock(inventario)
        elif eleccion == "c":
            nombre = input("Ingrese el nombre del producto: ")
            stock = int(input("Ingrese el stock del producto: "))
            inventario.agregar_producto(nombre, stock)
        elif eleccion == "d":
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif eleccion == "e":
            nombre_antiguo = input("Ingrese el nombre del producto a editar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
            inventario.actualizar_producto(nombre_antiguo, nuevo_nombre, nuevo_stock)
        elif eleccion == "f":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")
            
class Inventario:
    def __init__(self):
        self.productos = []
        productos_iniciales = [
            ("Peras", 20), ("Miel", 5), ("Queso panela", 15),
            ("Limones", 7), ("Leche", 8), ("Remolacha", 12),
            ("Jocote de corona", 3), ("Huevos", 9), ("Chocolate", 14),
            ("Guayaba", 11)
        ]
        for nombre, stock in productos_iniciales:
            self.agregar_producto(nombre, stock)

    def agregar_producto(self, nombre, stock):
        producto = Producto(nombre, stock)
        self.productos.append(producto)
        print(f"Producto agregado: {producto}")

    def bubble_sort(self):
        n = len(self.productos)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.productos[j].stock > self.productos[j+1].stock:
                    self.productos[j], self.productos[j+1] = self.productos[j+1], self.productos[j]

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            self.bubble_sort()
            for producto in self.productos:
                print(producto)

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"Producto eliminado: {producto}")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, nombre, nuevo_nombre, nuevo_stock):
        for producto in self.productos:
            if producto.nombre == nombre:
                producto.nombre = nuevo_nombre
                producto.stock = nuevo_stock
                print(f"Producto actualizado: {producto}")
                return
        print("Producto no encontrado.")

    def productos_con_bajo_stock(self):
        self.bubble_sort()
        return [producto for producto in self.productos if producto.stock < 10]

def menu_bajo_stock(inventario):
    productos_bajos = inventario.productos_con_bajo_stock()
    if not productos_bajos:
        print("No hay productos con bajo stock.")
        return

    print("\nProductos con bajo stock:")
    cantidad_mostrar = int(input("¿Cuántos productos desea ver?: "))
    for producto in productos_bajos[:cantidad_mostrar]:
        print(producto)
    
    if input("¿Desea reabastecer algún producto? (s/n): ").lower() == 's':
        nombre_producto = input("Ingrese el nombre del producto a reabastecer: ")
        cantidad_reabastecer = int(input("Ingrese la cantidad de stock a agregar: "))
        for producto in productos_bajos:
            if producto.nombre == nombre_producto:
                producto.stock += cantidad_reabastecer
                print(f"Producto {producto.nombre} reabastecido. Nuevo stock: {producto.stock}")
                break
        else:
            print("Producto no encontrado.")


inventario = Inventario()
menu_principal(inventario)
