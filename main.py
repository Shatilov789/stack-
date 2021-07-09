class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items

    def size(self):
        return len(self.items)


def is_balanced(text, brackets="〈〉()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    s1 = Stack()

    for character in text:
        if character in opening:
            s1.push(opening.index(character))

        elif character in closing:
            if s1.peek() and s1.peek()[-1] == closing.index(character):
                s1.pop()
            else:
                return "Несбалансированно"
    return  "Сбалансированно"


print(is_balanced('(((([{}]))))'))
print(is_balanced('[([])((([[[]]])))]{()}'))
print(is_balanced('{{[()]}}'))
print(is_balanced('}{}'))
print(is_balanced('{{[(])]}}'))
print(is_balanced('[[{())}]'))