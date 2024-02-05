#gestionDeInventarios

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.id != id]

    def actualizar_producto(self, id, nombre, cantidad, precio):
        for p in self.productos:
            if p.id == id:
                p.nombre = nombre
                p.cantidad = cantidad
                p.precio = precio
                break

    def buscar_producto(self, id):
        for p in self.productos:
            if p.id == id:
                return p
        return None

    def calcular_valor_total(self):
        total = 0
        for p in self.productos:
            total += p.cantidad * p.precio
        return total

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()

    producto1 = Producto(1, "Camiseta", 10, 20)
    producto2 = Producto(2, "Zapatos", 5, 50)

    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    print("Valor total del inventario:", inventario.calcular_valor_total())
