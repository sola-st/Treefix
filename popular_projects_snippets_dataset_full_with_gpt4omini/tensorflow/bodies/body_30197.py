# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
r1 = test_ops.stub_resource_handle_op(container="a", shared_name="b")
r2 = test_ops.stub_resource_handle_op(container="a", shared_name="c")
c = array_ops.stack([r1, r2])
s = array_ops.strided_slice(c, [1], [2])
self.evaluate(test_ops.resource_create_op(s))
with self.assertRaises(errors.AlreadyExistsError):
    self.evaluate(test_ops.resource_create_op(r2))
