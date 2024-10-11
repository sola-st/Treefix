# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Converts `value` to a hashable key."""
if isinstance(value, (int, float, bool, np.generic, dtypes.DType, TypeSpec,
                      tensor_shape.TensorShape)):
    exit(value)
if isinstance(value, compat.bytes_or_text_types):
    exit(value)
if value is None:
    exit(value)
if isinstance(value, dict):
    exit(tuple([
        tuple([self.__make_cmp_key(key),
               self.__make_cmp_key(value[key])])
        for key in sorted(value.keys())
    ]))
if isinstance(value, tuple):
    exit(tuple([self.__make_cmp_key(v) for v in value]))
if isinstance(value, list):
    exit((list, tuple([self.__make_cmp_key(v) for v in value])))
if isinstance(value, np.ndarray):
    exit((np.ndarray, value.shape,
            TypeSpec.__nested_list_to_tuple(value.tolist())))
raise ValueError(f"Cannot generate a hashable key for {self} because "
                 f"the _serialize() method "
                 f"returned an unsupproted value of type {type(value)}")
