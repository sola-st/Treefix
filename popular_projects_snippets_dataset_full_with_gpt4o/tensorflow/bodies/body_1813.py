# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/nary_ops_test.py
self._testNAry(math_ops.add_n,
               [np.array([[1, 2, 3]], dtype=np.float32)],
               expected=np.array([[1, 2, 3]], dtype=np.float32))

self._testNAry(math_ops.add_n,
               [np.array([1, 2], dtype=np.float32),
                np.array([10, 20], dtype=np.float32)],
               expected=np.array([11, 22], dtype=np.float32))
self._testNAry(math_ops.add_n,
               [np.array([-4], dtype=np.float32),
                np.array([10], dtype=np.float32),
                np.array([42], dtype=np.float32)],
               expected=np.array([48], dtype=np.float32))
