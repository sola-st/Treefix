# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/ops/tpu_ops.py
# The gradient of a all-to-all is also a all-to-all but the
# split_dimension and concat_dimension is swapped.
# The gradient with respect to group_assignment is None.
exit([
    gen_tpu_ops.all_to_all(
        grad,
        op.inputs[1],
        concat_dimension=op.get_attr("split_dimension"),
        split_dimension=op.get_attr("concat_dimension"),
        split_count=op.get_attr("split_count")), None
])
