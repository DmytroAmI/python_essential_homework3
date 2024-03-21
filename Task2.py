class English:
    """for example"""
    def __init__(self, language, country):
        """Initialize the class attribute"""
        self.language = language
        self.country = country

    def greeting(self):
        """Create a greeting"""
        return f"Hello from {self.country}"


class Spanish:
    """for example"""
    def __init__(self, language, country):
        """Initialize the class attribute"""
        self.language = language
        self.country = country

    def greeting(self):
        """Create a greeting"""
        return f"Hello from {self.country}"


def hello_friend(greeting1, greeting2):
    """Show greetings"""
    print(greeting1 + "\n" + greeting2)


english = English("English", "England")
spanish = Spanish("Spanish", "Spain")

hello_friend(english.greeting(), spanish.greeting())
