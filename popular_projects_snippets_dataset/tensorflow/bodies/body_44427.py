# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow_test.py
with self.assertRaisesRegex(ValueError, r"'s'.* shape \(1,\) after"):
    self._basic_loop(0, lambda i, s: np.array([1], dtype=np.int32))
