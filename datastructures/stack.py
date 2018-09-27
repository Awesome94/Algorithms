class Stack:
    def __init__(self):
        self.storage = ""

    def push(self, word):
        self.storage = self.storage + "-" + word

    def pop(self):
        word = self.storage[self.storage.rfind('-')+1:]
        self.storage = self.storage[:self.storage.rfind('-')]
        return word

    def size(self):
        return len(self.storage)

people = Stack()
people.push("awesome")
people.push("kironde")
people.push("daniel")
print(people.size())
print(people.storage)
last = people.pop()
print(last)
print(people.storage)
print(people.size())
