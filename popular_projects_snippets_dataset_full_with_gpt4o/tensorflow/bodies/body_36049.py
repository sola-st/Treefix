# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode():
    tmp_dir = self.get_temp_dir()
    fname = os.path.join(tmp_dir, "var.pickle")
    with open(fname, "wb") as f:
        v = resource_variable_ops.ResourceVariable(
            10.0,
            dtype=dtypes.float16,
            name="v")
        pickle.dump(v, f)

    with open(fname, "rb") as f:
        new_v = pickle.load(f)
        self.assertEqual(new_v.name, v.name)
        self.assertEqual(new_v.shape, v.shape)
        self.assertEqual(new_v.dtype, v.dtype)
        self.assertEqual(new_v.trainable, v.trainable)
        self.assertAllEqual(new_v.numpy(), v.numpy())
