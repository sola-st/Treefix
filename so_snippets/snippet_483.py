# Extracted from https://stackoverflow.com/questions/38727520/how-do-i-add-default-parameters-to-functions-when-using-type-hinting
def foo(opts: dict = {}):
    pass

print(foo.__annotations__)

{'opts': <class 'dict'>}

