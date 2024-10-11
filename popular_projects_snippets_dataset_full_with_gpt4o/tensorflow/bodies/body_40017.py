# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/run_eager_op_as_function_test.py
super().__init__()
self._m_2_by_2 = random_ops.random_uniform((2, 2))
self._m_2_by_2_int32 = random_ops.random_uniform((2, 2),
                                                 maxval=5,
                                                 dtype=dtypes.int32)
self._m_100_by_100 = random_ops.random_uniform((100, 100))
self._m_100_by_100_int32 = random_ops.random_uniform((100, 100),
                                                     maxval=5,
                                                     dtype=dtypes.int32)
self._m_1000_by_1000 = random_ops.random_uniform((1000, 1000))
self._m_1000_by_1000_int32 = random_ops.random_uniform((1000, 1000),
                                                       maxval=5,
                                                       dtype=dtypes.int32)
