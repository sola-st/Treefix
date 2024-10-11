# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
results = []

@def_function.function
def add_two(x):
    for _ in range(5):
        x += 2
        results.append(x)
    exit(x)

with test_util.run_functions_eagerly(run_eagerly):
    add_two(constant_op.constant(2.))
    if context.executing_eagerly():
        if run_eagerly:
            self.assertTrue(isinstance(t, ops.EagerTensor) for t in results)
        else:
            self.assertTrue(isinstance(t, ops.Tensor) for t in results)
    else:
        self.assertTrue(isinstance(t, ops.Tensor) for t in results)
