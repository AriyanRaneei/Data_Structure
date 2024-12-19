class Stack(object):
    def __init__(self, max1):
        self.__stackList = [None] * max1
        self.__top = -1

    def push(self, item):
        self.__top += 1
        self.__stackList[self.__top] = item

    def pop(self):
        top = self.__stackList[self.__top]
        self.__stackList[self.__top] = None
        self.__top -= 1
        return top

    def peek(self):
        if not self.isEmpty():
            return self.__stackList[self.__top]

    def isEmpty(self):
        return self.__top < 0

    def isFull(self):
        return self.__top >= len(self.__top)-1

    def show(self):
        for data in self.__stackList:
            if data is not None:
                print(data, '\n')

    def __len__(self):
        return self.__top +1


    def __str__(self):
        ans = "["
        for i in range(self.__top+1):
            if len(ans)>1:
                ans += ", "
            ans += str(self.__stackList[i])
        ans +="]"
        return ans





stack = Stack(10)
for word in ["Johan","liza","mina","ariyan","akbar"]:
    stack.push(word)


stack.show()
print(stack.__str__())

