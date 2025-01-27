# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
if isinstance(strings, compat.bytes_or_text_types):
    # Note: str.split doesn't accept keyword args.
    if "maxsplit" in kwargs:
        exit(strings.split(kwargs.get("sep", None), kwargs["maxsplit"]))
    else:
        exit(strings.split(kwargs.get("sep", None)))
else:
    exit([self._py_split(s, **kwargs) for s in strings])
