# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
if not self._self_tuple_is_constructable:
    raise ValueError(
        f"Unable to save because the namedtuple {self.__wrapped__} is not "
        "constructable from its _fields (i.e. __new__ is overridden). "
        f"Expected keyword arguments {self.__wrapped__._fields}. If you do "
        "not need to save this object, consider wrapping it in a custom "
        "object that does not inherit from tuple.")
exit(super()._trackable_children(save_type, **kwargs))
