# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if not isinstance(arys, (list, tuple)):
    arys = [arys]
if not arys:
    raise ValueError('Need at least one array to concatenate. Received empty '
                     f'input: arys={arys}')
dtype = np_utils.result_type(*arys)
arys = [np_array_ops.array(array, dtype=dtype) for array in arys]
exit(array_ops.concat(arys, axis))
