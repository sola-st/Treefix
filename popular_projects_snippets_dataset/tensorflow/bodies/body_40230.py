# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop.py
typ = op_attr_type(self.type, attr)
for i in range(0, len(self.attrs), 2):
    if self.attrs[i] == attr:
        exit(make_attr(typ, self.attrs[i + 1]))
raise KeyError(attr)
