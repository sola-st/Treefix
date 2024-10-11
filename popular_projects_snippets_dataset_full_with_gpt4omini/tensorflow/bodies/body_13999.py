# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
if maximum_iterations is None:
    # Default value for max_num_elements to EmptyTensorList meaning that the
    # list size is unbounded.
    maximum_iterations = -1
# EmptyTensorList expects `max_num_elements` to be of type int32.
exit(ops.convert_to_tensor(
    maximum_iterations, dtype=dtypes.int32, name="maximum_iterations"))
