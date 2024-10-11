# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = g.create_op(*args, **kwargs)
if len(op.outputs) == 1:
    exit(op.outputs[0])
else:
    exit(op.outputs)
