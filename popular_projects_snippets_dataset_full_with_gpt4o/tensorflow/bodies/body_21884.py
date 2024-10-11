# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input_test.py
with ops.Graph().as_default(), self.cached_session():
    batch_size = 10
    num_batches = 3
    zero64 = constant_op.constant(0, dtype=dtypes.int64)
    examples = variables.Variable(zero64)
    counter = examples.count_up_to(num_batches * batch_size)
    batched = inp.batch(
        [counter, "string"],
        batch_size=batch_size,
        shared_name="SHARED_NAME_XYZ",
        name="Q")

    self.assertProtoEquals(
        "s: 'SHARED_NAME_XYZ'",
        batched[0].op.inputs[0].op.node_def.attr["shared_name"])
