# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/partitioned_variables_test.py
with self.cached_session():
    rnd = variables.Variable(
        random_ops.random_uniform([20, 43], dtype=dtypes.float64))
    var_lists = [
        partitioned_variables.create_partitioned_variables(
            rnd.get_shape(), [1, i], rnd.initialized_value())
        for i in range(1, 10)
    ]
    self.evaluate(variables.global_variables_initializer())
    rnd_val = self.evaluate(rnd)
    # Only check the slice save specs for the first 5 tf.
    save_specs = [
        # One slice
        ["20 43 0,20:0,43"],
        # Two slices
        ["20 43 0,20:0,22", "20 43 0,20:22,21"],
        # Three slices
        ["20 43 0,20:0,15", "20 43 0,20:15,14", "20 43 0,20:29,14"],
        # Four slices
        [
            "20 43 0,20:0,11", "20 43 0,20:11,11", "20 43 0,20:22,11",
            "20 43 0,20:33,10"
        ],
        # Five slices
        [
            "20 43 0,20:0,9", "20 43 0,20:9,9", "20 43 0,20:18,9",
            "20 43 0,20:27,8", "20 43 0,20:35,8"
        ]
    ]
    for i, vs in enumerate(var_lists):
        var_val = array_ops.concat(vs, 1)
        self.assertAllClose(rnd_val, var_val)
        self.assertEqual([dtypes.float64] * len(vs),
                         [v.dtype.base_dtype for v in vs])
        if i < len(save_specs):
            self._TestSaveSpec(vs, save_specs[i])
