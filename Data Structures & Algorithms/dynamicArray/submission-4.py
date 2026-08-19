class DynamicArray:
    def __init__(self, capacity: int):
        if capacity > 0:
            self.the_array = [None] * capacity
            self.capacity = capacity
            self.size = 0
        else:
            raise ValueError("Capacity must be greater than 0.")
            
    def get(self, i: int) -> int:
        return self.the_array[i]

    def set(self, i: int, n: int) -> None:  
        self.the_array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()  # Resize only if the array is at full capacity
        self.the_array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.the_array[self.size - 1]
        self.size -= 1
        return value
    
    def resize(self):
        new_capacity = self.capacity * 2  # Double the capacity
        new_array = [None] * new_capacity

        # Copy elements to the new array
        for i in range(self.size):
            new_array[i] = self.the_array[i]

        # Update references to the new array and new capacity
        self.the_array = new_array
        self.capacity = new_capacity
    
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
