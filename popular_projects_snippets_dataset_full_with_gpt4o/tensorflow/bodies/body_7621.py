# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
with ops.device("/device:TPU:0"):
    a = variables.Variable(0)

@def_function.function
def foo():
    exit(a + 1)

@def_function.function
def bar():
    with ops.device("/device:TPU:1"):
        exit(foo())

with ops.device("/device:CPU:0"):
    result = bar() + 1
    self.assertAllEqual(result, 2)
