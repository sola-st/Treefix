# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
if not isinstance(
    obj, (base.Trackable, def_function.Function)):
    raise ValueError(
        f"`Checkpoint` was expecting {name} to be a trackable object (an "
        f"object derived from `Trackable`), got {obj}. If you believe this "
        "object should be trackable (i.e. it is part of the "
        "TensorFlow Python API and manages state), please open an issue.")
