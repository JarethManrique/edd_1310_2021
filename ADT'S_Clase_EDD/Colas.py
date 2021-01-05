class Queue:
    def __init__(self):
        self.__data = list() # []

    def is_empty(self):
        return len(self.__data) == 0

    def length(self):
        return len(self.__data)

    def enqueue(self, elem):
        self.__data.append(elem)

    def dequeue(self):
        if self.is_empty():
            print("Cola vacía")
        else:
            return self.__data.pop(0)

    def to_string(self):
        cadena = ""
        for elem in self.__data:
            cadena = cadena + " | " + str(elem)
        cadena = cadena + " | "
        return cadena
