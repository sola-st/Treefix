# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/variable_ops_test.py
for dtype in self.numeric_types:
    init = np.ones([2, 3]).astype(dtype)
    with self.session() as session, self.test_scope():
        v = resource_variable_ops.ResourceVariable(init)
        session.run(variables.variables_initializer([v]))
        h = v.handle
        s32, s64 = session.run([
            resource_variable_ops.variable_shape(h),
            resource_variable_ops.variable_shape(h, out_type=dtypes.int64)
        ])
        self.assertEqual(s32.dtype, np.int32)
        self.assertEqual(s64.dtype, np.int64)
        self.assertAllEqual(s32, [2, 3])
        self.assertAllEqual(s64, [2, 3])
