class Base:
    """Parent class"""
    @classmethod
    def method(cls):
        """Print greetings"""
        print("Hello from Base")


class Child(Base):
    """Child class"""
    @classmethod
    def method(cls):
        """Print greetings"""
        print("Hello from Child")


Base.method()
Child.method()
