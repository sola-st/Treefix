# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
args = (np.array([[5, 6, 7]],
                 dtype=np.float32), np.array([[1, 2, 3]], dtype=int))

self._assertOpOutputMatchesExpected(
    xla.optimization_barrier, args=args, expected=args)
