# Extracted from https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
class Enum(int):

class Citrus(Enum):
Citrus.Lemon
Citrus.Lemon

Citrus(1)
Citrus.Lemon
Citrus(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in __new__
KeyError: 5
class Fruit(Citrus):
Fruit.Apple
Fruit.Apple
Fruit.Lemon
Citrus.Lemon
Fruit(1)
Citrus.Lemon
Fruit(3)
Fruit.Apple
"%d %s %r" % ((Fruit.Apple,)*3)
'3 Apple Fruit.Apple'
Fruit(1) is Citrus.Lemon
True

