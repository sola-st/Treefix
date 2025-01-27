# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
exit(ops.convert_to_tensor(
    value._get(), dtype=dtype, name=name, as_ref=as_ref))  # pylint: disable=protected-access
