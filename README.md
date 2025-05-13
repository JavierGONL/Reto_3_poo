# Reto_3_poo

# ejercicio en clase
## Reto 3
1. Create a repo with the class exercise
```python
# Clase que representa un punto en un plano cartesiano
class Point:
    def __init__(self, x, y):
        self.x = x  # Coordenada x
        self.y = y  # Coordenada y

    # Método para crear un nuevo punto a partir de coordenadas dadas
    def another_point(self, new_x, new_y):
        return Point(new_x, new_y)


# Clase que representa una línea en un plano cartesiano
class Line:
    def __init__(self, inicio: "Point" = Point(0, 0), final: "Point" = Point(0, 0)):
        self.inicio = inicio  
        self.final = final  
        self.length = "you have to compute this first"  
        self.slope = "you have to compute this first"  
        self.range = "you have to compute this first" 

    # Método para calcular la longitud de la línea
    def compute_length(self):
        self.length = ((self.final.x - self.inicio.x) ** 2 + (self.final.y - self.inicio.y) ** 2) ** (1 / 2)
        return self.length

    # Método para calcular la pendiente de la línea
    def compute_slope(self):
        self.slope = (self.final.y - self.inicio.y) / (self.final.x - self.inicio.x)
        return self.slope

    # Método para calcular el rango de puntos de la línea
    def range_of_the_line(self):
        self.range = []
        if type(self.slope) != str:  # Verifica que la pendiente haya sido calculada
            for i in range(self.inicio.x, self.final.x):
                self.range.append(Point(i, (self.slope) * i)) 
            return self.range
        else:
            return print("you have to compute slope first")

    # Método para verificar si la línea cruza el eje x
    def horizontal_cross(self):
        for i in range(len(self.range), len(self.range) - 1):
            if self.range[i].x < 0 and self.range[i + 1].x > 0:
                return print(f"Cross the x-axis between {self.range[i]} and {self.range[i + 1]}")
        return print(f"don't Cross the x-axis")

    # Método para verificar si la línea cruza el eje y
    def vertical_cross(self):
        for i in range(len(self.range), len(self.range) - 1):
            if self.range[i].y < 0 and self.range[i + 1].y > 0:
                return print(f"Cross the y-axis between {self.range[i]} and {self.range[i + 1]}")
        return print(f"don't Cross the y-axis")


# Clase que representa un rectángulo
class Rectangle:
    def __init__(self, width, height, point_given, metod=1, oposite_corner=None, line_1=None, line_2=None):
        # Diferentes métodos para inicializar el rectángulo
        if metod == 1:  # Método 1: Usar el punto inferior izquierdo
            self.point_bottom_left: "Point" = point_given
            self.width: float = width
            self.height: float = height
        elif metod == 2:  # Método 2: Usar el punto central
            self.point_bottom_left: "Point" = point_given.another_point(
                point_given.x - width / 2, point_given.y - height / 2
            )
            self.width: float = width
            self.height: float = height
        elif metod == 3:  # Método 3: Usar dos esquinas opuestas
            self.point_bottom_left: "Point" = point_given
            self.width: float = abs(oposite_corner.x - point_given.x)
            self.height: float = abs(oposite_corner.y - point_given.y)
        elif metod == 4:  # Método 4: Usar dos líneas
            line_1 = line_1.range_of_the_line()
            line_2 = line_2.range_of_the_line()
            self.point_bottom_left: "Point" = line_1[0]
            self.width: float = abs(line_1[-1].x - line_1[0].x)
            self.height: float = abs(line_2[-1].y - line_2[0].y)

        # Inicialización de los puntos de las esquinas
        self.point_bottom_right: "Point"
        self.point_upper_left: "Point"
        self.point_upper_right: "Point"

    # Método para inicializar las esquinas del rectángulo
    def init_bottom_left(self):
        self.point_bottom_right = self.point_bottom_left.another_point(
            self.point_bottom_left.x + self.width, self.point_bottom_left.y
        )
        self.point_upper_left = self.point_bottom_left.another_point(
            self.point_bottom_left.x, self.point_bottom_left.y + self.height
        )
        self.point_upper_right = self.point_bottom_left.another_point(
            self.point_bottom_left.x + self.width, self.point_bottom_left.y + self.height
        )
        return [self.point_bottom_left, self.point_bottom_right, self.point_upper_left, self.point_upper_right]

    # Método para calcular el centro del rectángulo
    def compute_center(self):
        return Point(
            self.point_bottom_left.x + self.width / 2,
            self.point_bottom_left.y + self.height / 2,
        )

    # Método para calcular el área del rectángulo
    def compute_area(self):
        return self.width * self.height

    # Método para calcular el perímetro del rectángulo
    def compute_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Método para verificar si dos rectángulos interfieren
    def compute_interference_between_2_rectangles(self, square_2: "Square"):
        centro_1 = self.center
        centro_2 = square_2.center
        distancia = ((centro_2.x - centro_1.x) ** 2 + (centro_2.y - centro_1.y) ** 2) ** 0.5
        cateto_opuesto = centro_2.y - centro_1.y
        coseno = cateto_opuesto / distancia
        hipotenusa_square_1 = abs(coseno * (self.width / 2))
        hipotenusa_square_2 = abs((coseno * (square_2.width / 2)))
        if distancia <= hipotenusa_square_1 + hipotenusa_square_2:
            print(f"interfieren")
        else:
            print(f"no interfieren")

    # Método para verificar si un rectángulo interfiere con un punto
    def compute_interferece_between_rectangle_and_point(self, point: "Point"):
        centro_1 = self.center
        centro_2 = point
        distancia = ((centro_2.x - centro_1.x) ** 2 + (centro_2.y - centro_1.y) ** 2) ** 0.5
        cateto_opuesto = centro_2.y - centro_1.y
        coseno = cateto_opuesto / distancia
        hipotenusa_square_1 = abs(coseno * (self.width / 2))
        if distancia <= hipotenusa_square_1:
            print(f"interfieren")
        else:
            print(f"no interfieren")

    def compute_interference_between_rectangle_and_line(self, line: "Line"):
        centro_1 = self.center
        line = line.range_of_the_line()
        interfieren: bool = False
        for i in range(len(line)):
            distancia = (((line[i].x - centro_1.x)) ** 2 + (line[i].y - centro_1.y) ** 2) ** 0.5
            cateto_opuesto = line[i].y - centro_1.y
            coseno = cateto_opuesto / distancia
            if coseno == 0:
                hipotenusa_square_1 = self.width / 2
            else:
                hipotenusa_square_1 = abs(cateto_opuesto / coseno)
            if distancia <= hipotenusa_square_1:
                interfieren = True
                break
        return interfieren

class Square(Rectangle):
    def __init__(self, side, point_given, metod=1):
        super().__init__(side, side, point_given, metod)
        self.center: "Point" = self.compute_center()


if __name__ == "__main__":
    punto_2 = Point(1, 1)
    square = Square(2, punto_2)
    square.init_bottom_left()
    square_2 = Square(4, Point(2, 3))
    linea = Line(Point(1, 1), Point(2, 3))
    linea.compute_slope()
    linea.range_of_the_line()
    print(linea.range[0].y)
    print(square_2.compute_interference_between_rectangle_and_line(linea))
```

2. **Restaurant scenario:** You want to design a program to calculate the bill for a customer's order in a restaurant.
- Define a base class *MenuItem*: This class should have attributes like name, price, and a method to calculate the total price.
- Create subclasses for different types of menu items: Inherit from *MenuItem* and define properties specific to each type (e.g., Beverage, Appetizer, MainCourse). 
- Define an Order class: This class should have a list of *MenuItem* objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.

```python
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
```

