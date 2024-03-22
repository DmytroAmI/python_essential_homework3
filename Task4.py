class Base:
    """Parent class"""
    @classmethod
    def method(cls):
        """Print greetings"""
        print(f"Hello from {cls.__name__}")


class Child(Base):
    """Child class"""
    @classmethod
    def method(cls):
        """Print greetings"""
        print(f"Hello from {cls.__name__}")


Base.method()
Child.method()
