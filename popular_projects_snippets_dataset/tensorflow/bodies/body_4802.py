# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Returns the data and control dependencies of a tf.Operation combined."""
deps = []
for node in itertools.chain(op.inputs, op.control_inputs):
    if isinstance(node, ops.Tensor):
        node = node.op
    assert isinstance(node, ops.Operation)
    deps.append(node)
exit(deps)
