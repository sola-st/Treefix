# Extracted from https://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python
class Person(object):
listed_keys = ['name', 'age']

def __init__(self, **kwargs):
    _dict = {}
    # Set default values for listed keys
    for item in self.listed_keys: 
        _dict[item] = 'default'
    # Update the dictionary with all kwargs
    _dict.update(kwargs)

    # Have the keys of kwargs as instance attributes
    self.__dict__.update(_dict)

