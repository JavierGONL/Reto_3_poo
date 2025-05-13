# Definimos la clase MenuItem como la clase base para los elementos del menú
class MenuItem:
    def __init__(self, name, price):
        self.name = name  # Nombre del elemento del menú
        self.price = price  # Precio del elemento del menú
    
    # Método para calcular el precio total basado en la cantidad de elementos
    def total_price(self, number_of_items):
        return self.price * number_of_items


# Clase MainCourse que hereda de MenuItem, representa los platos principales
class MainCourse(MenuItem):
    definition = "el plato principal"  # Definición en español
    def __init__(self, name, price):
        super().__init__(name, price)  # Llama al constructor de la clase base


# Clase Drinks que hereda de MenuItem, representa las bebidas
class Drinks(MenuItem):
    definition = "las bebidas"  # Definición en español
    def __init__(self, name, price):
        super().__init__(name, price)  # Llama al constructor de la clase base
        

# Clase Dessert que hereda de MenuItem, representa los postres
class Dessert(MenuItem):
    definition = "el postre"  # Definición en español
    def __init__(self, name, price):
        super().__init__(name, price)  # Llama al constructor de la clase base


# Clase Order que representa una orden de un cliente
class Order:
    def __init__(self):
        self.main_course = None  # Plato principal en la orden
        self.drink = None  # Bebida en la orden
        self.dessert = None  # Postre en la orden
        self.order_total_price = 0  # Precio total de la orden
        self.number_items_order = 0

    # Método para agregar un plato principal a la orden
    def add_main_course(self, main_course, number_of_items=1):
        self.main_course = main_course
        self.number_items_order += 1
        self.order_total_price += main_course.total_price(number_of_items)

    # Método para agregar una bebida a la orden
    def add_drink(self, drink, number_of_items=1):
        self.drink = drink
        self.number_items_order += 1
        self.order_total_price += drink.total_price(number_of_items)

    # Método para agregar un postre a la orden
    def add_dessert(self, dessert, number_of_items=1):
        self.dessert = dessert
        self.number_items_order += 1
        self.order_total_price += dessert.total_price(number_of_items)

    # Método para obtener el precio total de la orden
    def get_total_price(self):
        if self.number_items_order >= 10 or self.order_total_price >= 100000:
            return (self.order_total_price - (self.order_total_price * 20/100))
        else:
            return self.order_total_price
    



# Bloque principal del programa
if __name__ == "__main__":
    # Listas de elementos del menú
    main_course_list = [
        MainCourse("frijolada", 10000),
        MainCourse("costillas bbq", 15000),
        MainCourse("pollo asado", 12000),
        MainCourse("tacos", 8000)
    ]
    drinks_list = [
        Drinks("agua", 2000),
        Drinks("limonada", 3000),
        Drinks("cafe", 2500),
        Drinks("cerveza", 5000)
    ]

    dessert_list = [
        Dessert("cupcake", 4000),
        Dessert("helado", 3500),
        Dessert("fruta", 3000),
        Dessert("chocolate", 4500)
    ]

    bandera = True  # Variable para controlar el ciclo del programa

    while bandera:
        order = Order()  # Crear una nueva orden
        print("¿Qué le gustaría agregar a la orden? " \
        "\n 1. Plato principal \n 2. Bebida \n 3. Postre")
        print("Siempre que desee salir escriba 0")
        seleccion_1 = int(input("-> "))  # Leer la selección del usuario
        if seleccion_1 == 1:
            print("¿Qué plato le gustaría?")
            for i in range(len(main_course_list)):
                print(f"{i+1}. {main_course_list[i].name}")  # Mostrar opciones de platos principales
        elif seleccion_1 == 2:
            print("¿Qué bebida le gustaría?")
            for i in range(len(drinks_list)):
                print(f"{i+1}. {drinks_list[i].name}")  # Mostrar opciones de bebidas
        elif seleccion_1 == 3:
            print("¿Qué postre le gustaría?")
            for i in range(len(dessert_list)):
                print(f"{i+1}. {dessert_list[i].name}")  # Mostrar opciones de postres
        elif seleccion_1 == 0:
            break  # Salir del ciclo si el usuario selecciona 0
        seleccion_2 = int(input("-> "))  # Leer la selección del usuario
        print("¿Cuántos desea?")
        seleccion_3 = int(input("-> "))  # Leer la cantidad deseada
        if seleccion_1 == 1:
            order.add_main_course(main_course_list[seleccion_2-1], seleccion_3)  # Agregar plato principal
        elif seleccion_1 == 2:
            order.add_drink(drinks_list[seleccion_2-1], seleccion_3)  # Agregar bebida
        elif seleccion_1 == 3:
            order.add_dessert(dessert_list[seleccion_2-1], seleccion_3)  # Agregar postre
        print("¿Desea agregar algo más a la orden?")
        seleccion_4 = int(input("1. Sí \n2. No\n-> "))  # Preguntar si desea agregar más elementos
        if seleccion_4 == 2:
            print(f"El total de su orden es: {order.get_total_price()}")  # Mostrar el total de la orden
            bandera = False  # Finalizar el ciclo
        else:
            bandera = True  # Continuar el ciclo
