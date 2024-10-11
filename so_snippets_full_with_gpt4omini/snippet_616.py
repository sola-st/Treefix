# Extracted from https://stackoverflow.com/questions/2675028/list-attributes-of-an-object
class new_class():
a = new_class(2)
a.__dict__
{'multi': 4, 'str': '2'}
a.__dict__.keys()
dict_keys(['multi', 'str'])

