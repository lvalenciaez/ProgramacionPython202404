



# es un molde a partir del cual podre crear objetos de tipo cliente
class Cliente:
    """Clase cliente"""
    # constantes
    total_articulos_comprados = 0

    def __init__(self, correo, telefono):
        """Metodo constructor"""
        # lo que si o requiero para crear un objeto de tipo cliene
        self.correo = correo
        self.telefono = telefono
        pass
    def realizar_pedido(self):
        """Permite solicitar una cantidad de pedidos"""
        cantidad_articulos = int(input('Cuantos articulos desea pedir? '))
        print(f'Ha realiazdo la compra de {cantidad_articulos}')
        self.total_articulos_comprados += cantidad_articulos
        pass

    def cancelar_pedido(self):
        """Permite cancelar un número x de mi pedido"""
        pedidos_cancelar = int(input('Cuanto articulos desea cancelar su pedido'))
        print(f'Ha cancelado la comprar de {pedidos_cancelar} articulos')
        self.total_articulos_comprados -= pedidos_cancelar
        pass

    def cantidad_total_comprado(self):
        return self.total_articulos_comprados
    
# A partir de mi molde, puedo crear objetos o clientes

cliente1 = Cliente(correo='lara@company.com', telefono='945123552')
cliente2 = Cliente(correo='tea@company.com', telefono='5451221532')
cliente3 = Cliente(correo='dave@company.com', telefono='948751215')

listado_clientes = [cliente1, cliente2, cliente3]


# Podemos ver nombre y correo de cliente
for i, cliente in enumerate(listado_clientes):

    # Por cada cliente muestro su correo y telefono

    print(f"""Mostrando datos para cliente {i}

    {cliente.correo} || {cliente.telefono}
    """)

    # por cada cliente solicito cuantos articulos quiere comprar

    cliente.realizar_pedido()
    pass










