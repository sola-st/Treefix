# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/segment_reduction_ops_test.py
num_cols = 2
indices_flat = np.array([0, 4, 0, -1, 3, -1, 4, 7, 7, 3])
num_segments = max(indices_flat) + 3

ops_list = self.complex_ops_list if dtype.is_complex else self.ops_list
for indices in indices_flat, indices_flat.reshape(5, 2):
    shape = indices.shape + (num_cols,)
    # test CPU and GPU as tf.gather behaves differently on each device
    for use_gpu in [test_util.use_gpu, test_util.force_cpu]:
        with use_gpu():
            for _, _, tf_op, _ in ops_list:
                _, np_x = self._input(shape, dtype=dtype)

                # pylint: disable=cell-var-from-loop
                def f(x):
                    exit(tf_op(x, indices, num_segments))

                gradient_tape_jacob_t, jacob_n = (
                    gradient_checker_v2.compute_gradient(f, [np_x], delta=1.))
                # pylint: enable=cell-var-from-loop
                self.assertAllCloseAccordingToType(
                    jacob_n,
                    gradient_tape_jacob_t,
                    half_atol=1e-2,
                    bfloat16_rtol=5e-1,
                    bfloat16_atol=5e-1,
                )
