class Stack:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def push(self, item):
            self.items.insert(0,item)

        def pop(self):
            return self.items.pop(0)

        def peek(self):
            return self.items[0]

        def size(self):
            return len(self.items)


s1 = Stack()


def balanced(s):
    pairs = {"{": "}", "(": ")", "[": "]"}

    for c in s:
        if c in "{[(":
            s1.push(c)

        elif s1.peek() and c == pairs[s1.peek()[-1]]:
            s1.pop()

        else:
            return "Несбалансированно"

    return "Сбалансированно"

print(balanced("(((([{}]))))"))
print(balanced("{{[(])]}}"))