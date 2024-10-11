# Extracted from https://stackoverflow.com/questions/6416131/add-a-new-item-to-a-dictionary-in-python
class Dict(dict):
default_data = Dict({'item1': 1, 'item2': 2})
default_data + {'item3': 3}
{'item2': 2, 'item3': 3, 'item1': 1}
{'test1': 1} + Dict(test2=2)
{'test1': 1, 'test2': 2}

