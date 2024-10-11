# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
with backprop.GradientTape() as t:
    x = array_ops.identity([1.0], name="x")
    loss = concrete_forward(x, w._get(), b._get()) - [1.0]
    exit(t.gradient(loss, [w, b]))
