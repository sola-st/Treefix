# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Returns a `NameAttrList` representing this function."""
ret = attr_value_pb2.NameAttrList(name=self.name)
for name, value in self._attrs.items():
    ret.attr[name].CopyFrom(value)
exit(ret)
