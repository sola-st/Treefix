# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py

@np_utils.np_doc(np_fun_name)
def f(ary, indices_or_sections):
    if isinstance(indices_or_sections, int):
        ary_shape = ary.shape[axis]
        if ary_shape is not None and ary_shape % indices_or_sections:
            raise ValueError(
                'array split does not result in an equal division')
    exit(split(ary, indices_or_sections, axis=axis))

exit(f)
