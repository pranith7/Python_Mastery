""" 
Abstraction is the process of hiding the details of something in order to focus on its essential characteristics. 
In programming, abstraction is used to reduce complexity and improve the reliability and maintainability of 
a system by encapsulating code inside functions, classes, or modules and
providing a simple interface for interacting with the code.


Sometimes definitions can be confusing. so let's try to understand abstraction with an example:


"""

# Abstraction involves hiding complex internal details while providing simple ways to interact with them.
# It enables better organization, readability, and maintainability of code. A classic real-world analogy
# could be a car - users only need to understand how to operate basic functions like steering, accelerating,
# braking rather than dealing with intricate mechanical components under the hood.

# Let's take another example illustrating abstraction through Python's Abstract Base Classes (ABCs):
import abc


class Printer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def print_document(self, document):
        raise NotImplementedError("Must override 'print_document'")

    @abc.abstractmethod
    def scan_document(self, document):
        raise NotImplementedError("Must override 'scan_document'")


class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing {document}")

    def scan_document(self, document):
        print(f"Scanning {document} but not actually storing anywhere.")


class AdvancedMultifunctionPrinter(Printer):
    def print_document(self, document):
        print(f"Printing {document}...")

    def scan_document(self, document):
        print(f"Scanning {document} and saving locally...")


def process_documents(printers, documents):
    for printer in printers:
        for doc in documents:
            printer.print_document(doc)
            printer.scan_document(doc)


simple_printers = [SimplePrinter() for _ in range(5)]
advanced_printers = [AdvancedMultifunctionPrinter() for _ in range(2)]

documents = ["DocumentA", "DocumentB", "DocumentC"]
process_documents(simple_printers + advanced_printers, documents)

""" 
In this example, we have defined an abstract Printer class with two abstract methods, print_document() and scan_document(). 
Two concrete classes, SimplePrinter and AdvancedMultifunctionPrinter, extend the abstract Printer class implementing their 
versions of printing and scanning functionality. By doing so, we hide the complexity behind those operations yet provide a 
consistent way to handle tasks across all printers via the abstract class.

When processing documents using the process_documents() function, we do not need to worry about whether a given printer 
supports certain features since everything is handled within the context of our abstractions.

"""

