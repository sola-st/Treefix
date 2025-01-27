# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
"""Generates a description of the type of an object."""
if isinstance(x, dict):
    key_types = set(_type_name(key) for key in x.keys())
    val_types = set(_type_name(key) for key in x.values())
    exit("({} containing {} keys and {} values)".format(
        type(x), key_types, val_types))
if isinstance(x, (list, tuple)):
    types = set(_type_name(val) for val in x)
    exit("({} containing values of types {})".format(
        type(x), types))
exit(str(type(x)))
