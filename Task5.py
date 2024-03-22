from PIL import Image, ImageDraw


class Shape:
    """Describe the parent class shape"""
    def __init__(self):
        """Initiate the attributes, set the color, create an image"""
        self.back_color = (155, 213, 117, 100)
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        """Needs to be overridden in a descendant"""
        pass

    def erase(self):
        """Erase the image"""
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self):
        """Save the image in .png format"""
        print("Background was created")
        return self.im.save('picture.png', quality=95)


class Circle(Shape):
    """Describe the Circle figure"""
    def draw(self):
        """Draw the circle"""
        self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))

    def erase(self):
        """Erase the circle"""
        self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)

    def save(self):
        """Save the image in .png format"""
        print("Image with circle was created")
        return self.im.save('draw-circle.png', quality=95)


class Square(Shape):
    """Describe the Square figure"""
    def draw(self):
        """Draw the square"""
        self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))

    def erase(self):
        """Erase the square"""
        self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)

    def save(self):
        """Save the image in .png"""
        print("Image with square was created")
        return self.im.save('draw-square.png', quality=95)


class Triangle(Shape):
    """Describe the Triangle figure"""
    def draw(self):
        """Draw the triangle"""
        self.draw1.polygon([(400, 100), (350, 200), (400, 200)], fill=(255, 255, 255))

    def erase(self):
        """Erase the triangle"""
        self.draw1.polygon([(400, 100), (350, 200), (400, 200)], fill=self.back_color)

    def save(self):
        """Save the image in .png format"""
        print("Image with triangle was created")
        return self.im.save('draw-triangle.png', quality=95)


class Paraboloid(Shape):
    """Describe the 2d Paraboloid figure"""
    def draw(self):
        """Draw the paraboloid"""
        self.draw1.ellipse((10, 10, 150, 275), fill='yellow', outline=(255, 255, 255))
        self.draw1.rectangle((10, 10, 300, 150), fill=self.back_color)

    def erase(self):
        """Erase the paraboloid"""
        self.draw1.ellipse((10, 10, 150, 275), fill=self.back_color)

    def save(self):
        """Save the image in .png format"""
        print("Image with 2d paraboloid was created")
        return self.im.save('draw-paraboloid.png', quality=90)


class Cone(Shape):
    """Describe the 2d Cone figure"""
    def draw(self):
        """Draw the cone"""
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))

    def erase(self):
        """Erase the cone"""
        self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)

    def save(self):
        """Save the image in .png format"""
        print("Image with 2d cone was created")
        return self.im.save('draw-cone.png', quality=95)


def work_with_obj(obj):
    """Draw and save the figure"""
    obj.draw()
    obj.save()


def update_obj(obj):
    """Erase and save the figure"""
    obj.erase()
    obj.save()


def menu():
    """Create the program menu"""
    while True:
        value = int(input(
            '\nМЕНЮ:\n\t1. Cтворити тло\n\t'
            '2. Cтворити коло\n\t'
            '3. Cтворити квадрат\n\t'
            '4. Cтворити трикутник\n\t'
            '5. Створити параболоїд\n\t'
            '6. Створити конус\n\t'
            '7. Зафарбувати коло\n\t'
            '8. Зафарбувати квадрат\n\t'
            '9. Зафарбувати трикутник\n\t'
            '10. Зафарбувати параболоїд\n\t'
            '11. Зафарбувати конус\n\t'
            '12. Вихід з програми\nОберіть необхідний пункт меню: '))

        match value:
            case 1:
                s = Shape()
                s.save()
            case 2:
                c = Circle()
                work_with_obj(c)
            case 3:
                sq = Square()
                work_with_obj(sq)
            case 4:
                t = Triangle()
                work_with_obj(t)
            case 5:
                p = Paraboloid()
                work_with_obj(p)
            case 6:
                cone = Cone()
                work_with_obj(cone)
            case 7:
                c = Circle()
                update_obj(c)
            case 8:
                sq = Square()
                update_obj(sq)
            case 9:
                t = Triangle()
                update_obj(t)
            case 10:
                p = Paraboloid()
                update_obj(p)
            case 11:
                cone = Cone()
                update_obj(cone)
            case 12:
                break
            case _:
                print('Оберіть пункт меню корректно!!!')


if __name__ == '__main__':
    menu()
