# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/run_metadata_test.py
# Note: Please don't just adjust the test to make it pass.
# The code view logic depends on it.
ops.reset_default_graph()
_, _ = _run_loop_model()
graph = ops.get_default_graph()
forward_op = set()
backward_op = set()
back_to_forward = {}
for op in graph.get_operations():
    if op.name.find('gradients/') > 0 and op.name.find('_grad/') > 0:
        backward_op.add(op.name)
        idx1 = op.name.find('gradients/') + 10
        idx2 = op.name.find('_grad/')
        back_to_forward[op.name] = op.name[idx1:idx2]
    else:
        forward_op.add(op.name)

for _, f in back_to_forward.items():
    self.assertTrue(f in forward_op)
