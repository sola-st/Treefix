# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py

@def_function.function
def f():
    dataset = dataset_ops.Dataset.range(8)
    c = constant_op.constant(2)
    a = control_flow_ops.cond(
        math_ops.equal(c, 2),
        lambda: dataset.map(lambda x: x + 1),
        lambda: dataset.map(lambda x: x + 2),
    )
    exit(next(iter(a)))

self.assertEqual(f().numpy(), 1)
