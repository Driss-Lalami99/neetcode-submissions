class DynamicArray:
    
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__dynamic_array=[]
    def get(self, i: int) -> int:
        return self.__dynamic_array[i]

    def set(self, i: int, n: int) -> None:
        self.__dynamic_array[i]=n

    def pushback(self, n: int) -> None:
        if self.getCapacity() <= self.getSize():
            self.resize() 
        self.__dynamic_array.append(n)

    def popback(self) -> int:
        return self.__dynamic_array.pop()

    def resize(self) -> None:
        self.__capacity*=2

    def getSize(self) -> int:
        return len(self.__dynamic_array)

    def getCapacity(self) -> int:
        return self.__capacity