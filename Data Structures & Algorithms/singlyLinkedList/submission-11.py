class LinkedList:
    
    def __init__(self):
        self.__linkedList= []
    
    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.__linkedList) :
            return -1 
        return self.__linkedList[index]

    def insertHead(self, val: int) -> None:
        self.__linkedList.insert(0,val)
           
    def insertTail(self, val: int) -> None:
        self.__linkedList.append(val)   

    def remove(self, index: int) -> bool:
        if index < 0 or index >= len(self.__linkedList) :
            return False
        self.__linkedList.pop(index)
        return True

    def getValues(self) -> List[int]:
        return  self.__linkedList
