class Temperature:
    """Describe the temperature class"""
    def __init__(self, degrees, scale):
        """Initiate the attributes"""
        self._degrees = degrees
        self._scale = scale

    def __str__(self):
        """Return a string representation of the temperature"""
        return f"The temperature is {self._degrees} {self._scale}"

    @property
    def degrees(self):
        """Access to read degrees"""
        return self._degrees

    @property
    def scale(self):
        """Access to read scale"""
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Set scale value, and change degrees value if it needs"""
        if scale == "Celsius" and self._scale == "Fahrenheit":
            self._degrees = (self._degrees - 32) * 5 / 9
        elif scale == "Fahrenheit" and self._scale == "Celsius":
            self._degrees = self._degrees * 9 / 5 + 32

        self._scale = scale


temp1 = Temperature(23, "Celsius")
temp2 = Temperature(73, "Fahrenheit")
print(temp1)
print(temp2)

temp1.scale = "Fahrenheit"
print(temp1)

temp2.scale = "Celsius"
print(temp2)
