# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
del inputs, attrs, op_name, graph  # Unused.
if op_type in ("Const", "Placeholder"):
    exit(outputs)
else:
    exit([math_ops.cast(output, dtypes.float64) for output in outputs])
