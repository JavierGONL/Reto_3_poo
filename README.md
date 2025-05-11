# Reto_3_poo

# ejercicio en clase

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
