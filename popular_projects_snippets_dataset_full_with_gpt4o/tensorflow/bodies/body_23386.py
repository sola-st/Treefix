# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
exit(("Only trackable objects (such as Layers or Optimizers) may be "
        f"stored in a List object. Got {self._value}, which does not "
        "inherit from Trackable."))
