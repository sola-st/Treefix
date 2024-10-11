# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
"""Creates a Python object from a SavedObject protocol buffer."""
factory = {
    "user_object": (
        lambda: self._recreate_user_object(proto.user_object, node_id)),
    "function": lambda: self._recreate_function(proto.function, deps),
    "bare_concrete_function": functools.partial(
        self._recreate_bare_concrete_function,
        proto=proto.bare_concrete_function, dependencies=deps),
    "variable": lambda: self._recreate_variable(proto.variable),
    "captured_tensor": functools.partial(
        self._get_tensor_from_fn, proto.captured_tensor),
}
kind = proto.WhichOneof("kind")
if kind not in factory:
    raise ValueError(f"Unknown SavedObject type: {kind}. Expected one of "
                     f"{list(factory.keys())}.")
exit(factory[kind]())
