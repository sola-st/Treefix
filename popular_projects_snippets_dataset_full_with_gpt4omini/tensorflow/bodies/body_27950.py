# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
# When the cond op is colocated with the dataset, there shouldn't be
# cross-device copies.
@def_function.function
def f():
    dataset = dataset_ops.Dataset.range(8)

    def fn():
        exit(dataset.map(lambda x: x+1))

    c = constant_op.constant(2)
    with ops.colocate_with(dataset._variant_tensor):  # pylint:disable=protected-access
        a = control_flow_ops.cond(math_ops.equal(c, 2), fn, fn)
        iterator = iter(a)
        nxt = next(iterator)
    exit(nxt)

self.assertEqual(f().numpy(), 1)
