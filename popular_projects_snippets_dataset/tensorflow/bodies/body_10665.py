# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
accumulator_ref = gen_data_flow_ops.sparse_conditional_accumulator(
    dtype=dtype,
    shape=shape,
    shared_name=shared_name,
    name=name,
    reduction_type=reduction_type)
super(SparseConditionalAccumulator, self).__init__(dtype, shape,
                                                   accumulator_ref)
