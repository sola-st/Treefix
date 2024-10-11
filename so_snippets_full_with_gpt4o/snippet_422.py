# Extracted from https://stackoverflow.com/questions/19151/how-to-build-a-basic-iterator
# generator
def uc_gen(text):
    for char in text.upper():
        yield char

# generator expression
def uc_genexp(text):
    return (char for char in text.upper())

# iterator protocol
class uc_iter():
    def __init__(self, text):
        self.text = text.upper()
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

# getitem method
class uc_getitem():
    def __init__(self, text):
        self.text = text.upper()
    def __getitem__(self, index):
        return self.text[index]

for iterator in uc_gen, uc_genexp, uc_iter, uc_getitem:
    for ch in iterator('abcde'):
        print(ch, end=' ')
    print()

A B C D E
A B C D E
A B C D E
A B C D E

    # for uc_iter we add __reversed__ and update __next__
    def __reversed__(self):
        self.index = -1
        return self
    def __next__(self):
        try:
            result = self.text[self.index]
        except IndexError:
            raise StopIteration
        self.index += -1 if self.index < 0 else +1
        return result

    # for uc_getitem
    def __len__(self)
        return len(self.text)

# generator
def even_gen():
    result = 0
    while True:
        yield result
        result += 2


# generator expression
def even_genexp():
    return (num for num in even_gen())  # or even_iter or even_getitem
                                        # not much value under these circumstances

# iterator protocol
class even_iter():
    def __init__(self):
        self.value = 0
    def __iter__(self):
        return self
    def __next__(self):
        next_value = self.value
        self.value += 2
        return next_value

# getitem method
class even_getitem():
    def __getitem__(self, index):
        return index * 2

import random
for iterator in even_gen, even_genexp, even_iter, even_getitem:
    limit = random.randint(15, 30)
    count = 0
    for even in iterator():
        print even,
        count += 1
        if count >= limit:
            break
    print

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32

