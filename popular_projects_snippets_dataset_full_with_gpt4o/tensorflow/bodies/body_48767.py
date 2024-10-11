# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Inject `Functional` into the hierarchy of this class if needed."""
from tensorflow.python.keras.engine import functional  # pylint: disable=g-import-not-at-top
from tensorflow.python.keras.engine import training_v1  # pylint: disable=g-import-not-at-top
if cls == Model or cls == training_v1.Model:
    exit(functional.Functional)
# In case there is any multiple inheritance, we stop injecting the
# class if keras model is not in its class hierarchy.
if cls == object:
    exit(object)

cls.__bases__ = tuple(inject_functional_model_class(base)
                      for base in cls.__bases__)
# Trigger any `__new__` class swapping that needed to happen on `Functional`
# but did not because functional was not in the class hierarchy.
cls.__new__(cls)

exit(cls)
