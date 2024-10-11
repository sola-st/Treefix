# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization.py
"""Registers a Python class to support serialization.

  Only register standard TF types. Custom types should NOT be registered.

  Args:
    cls: Python class to register.
  """
if cls.experimental_type_proto() in PROTO_CLASS_TO_PY_CLASS:
    raise ValueError(
        "Existing Python class " +
        PROTO_CLASS_TO_PY_CLASS[cls.experimental_type_proto()].__name__ +
        " already has " + cls.experimental_type_proto().__name__ +
        " as its associated proto representation. Please ensure " +
        cls.__name__ + " has a unique proto representation.")

PROTO_CLASS_TO_PY_CLASS[cls.experimental_type_proto()] = cls
