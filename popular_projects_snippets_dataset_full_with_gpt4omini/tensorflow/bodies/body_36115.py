# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    init = array_ops.ones(shape=[10, 20, 35], dtype=dtypes.int32)
    constraint = lambda x: x
    with ops.name_scope("foo", skip_on_eager=False):
        v = resource_variable_ops.ResourceVariable(
            name="var7",
            initial_value=init,
            caching_device="cpu:0",
            constraint=constraint)
    # Test properties
    self.assertEqual(dtypes.int32, v.dtype)
    self.assertEqual("foo/var7:0", v.name)
    self.assertAllEqual([10, 20, 35], v.shape.as_list())
    self.assertIsInstance(v.handle, ops.EagerTensor)
    self.assertEqual(constraint, v.constraint)
    self.assertAllEqual(init.numpy(), v.read_value().numpy())
    self.assertAllEqual(init.numpy(), v.value().numpy())

    # Callable init.
    callable_init = lambda: init * 2
    v2 = resource_variable_ops.ResourceVariable(
        initial_value=callable_init, name="var7")
    self.assertEqual("var7:0", v2.name)
    self.assertAllEqual(2 * init.numpy(), v2.read_value().numpy())

    # Test assign_add.
    new_v2_val = v2.assign_add(v.read_value())
    self.assertAllEqual(v.read_value().numpy() * 3, new_v2_val.numpy())

    # Test assign_sub.
    new_v2_val = v2.assign_sub(v.read_value())
    self.assertAllEqual(v.read_value().numpy() * 2, new_v2_val.numpy())

    # Test assign.
    v2.assign(v.read_value())
    self.assertAllEqual(v.read_value().numpy(), v2.read_value().numpy())

    # Test load
    v2.load(2 * v.read_value())
    self.assertAllEqual(2 * v.read_value().numpy(), v2.read_value().numpy())

    # Test convert_to_tensor
    t = ops.convert_to_tensor(v)
    self.assertAllEqual(t.numpy(), v.read_value().numpy())

    # Test operations
    self.assertAllEqual((v * 2).numpy(), (v + v).numpy())
