# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
super(AlreadyGarbageCollectedError,
      self).__init__(f"{name} of type {obj_type} has already been garbage "
                     f"collected and cannot be called.")
