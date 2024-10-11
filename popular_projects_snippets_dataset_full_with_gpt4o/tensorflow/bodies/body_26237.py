# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
exit([
    ops.convert_to_tensor(
        tf_nest.map_structure(lambda x: x._variant_tensor, value))  # pylint: disable=protected-access
])
