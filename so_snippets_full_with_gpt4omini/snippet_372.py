# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
from l3.Runtime import _l_
def print_msg(msg):
    _l_(456)

    # This is the outer enclosing function

    def printer():
        _l_(454)

        # This is the nested function
        print(msg)
        _l_(453)
    aux = printer  # returns the nested function
    _l_(455)  # returns the nested function

    return aux  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
_l_(457)
another()
_l_(458)

