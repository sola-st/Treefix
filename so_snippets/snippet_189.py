# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/472000/usage-of-slots
from l3.Runtime import _l_
class Person:
    _l_(2428)


    __slots__ = {
        "birthday":
            "A datetime.date object representing the person's birthday.",
        "name":
            "The first and last name.",
        "public_variable":
            None,
        "_private_variable":
            "Description",
    }
    _l_(2427)


help(Person)
_l_(2429)
"""
Help on class Person in module __main__:

class Person(builtins.object)
 |  Data descriptors defined here:
 |
 |  birthday
 |      A datetime.date object representing the person's birthday.
 |
 |  name
 |      The first and last name.
 |
 |  public_variable
"""

