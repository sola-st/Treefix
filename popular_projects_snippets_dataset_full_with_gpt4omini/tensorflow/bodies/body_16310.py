# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nccl_ops_test.py
"""Tests that nccl_reduce does the same as reduction with numpy_fn.

    Args:
      nccl_reduce: A function taking a list of tensors and a list of devices,
          and returns a list of reduced tensors and a list of ops to perform the
          reduction.
      numpy_fn: A function taking two tensors and returning the reduction of the
          two.
      device_sets: Tuple of virtual devices to run test on.
    """
for dtype in [np.float16, np.float32, np.int32, np.int64, np.float64]:
    # Create session inside outer loop to test use of
    # same communicator across multiple sessions.
    with self.test_session():

        for devices in device_sets:
            shape = (3, 4)
            random = (np.random.random_sample(shape) - .5) * 1024
            tensors = []
            for _ in devices:
                tensors.append(random.astype(dtype))
            np_ans = tensors[0]
            for t in tensors[1:]:
                np_ans = numpy_fn(np_ans, t)

            reduce_tensors = nccl_reduce(tensors, devices)
            self.assertNotEmpty(reduce_tensors)

            # Test shape inference.
            for r in reduce_tensors:
                self.assertEqual(shape, r.get_shape())

            result_tensors = [array_ops.identity(t) for t in reduce_tensors]

            # Check GPU availability *after* creating session, see b/68975239.
            if not test.is_gpu_available():
                # If no GPU is available, only test graph construction.
                continue

            # Test execution and results.
            for t in self.evaluate(result_tensors):
                self.assertAllClose(t, np_ans)
