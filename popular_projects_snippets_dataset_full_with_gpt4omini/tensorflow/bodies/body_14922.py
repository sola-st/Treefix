# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
with self.assertRaisesRegex(TypeError, "only takes keyword args"):
    gen_math_ops.Add(1., 1.)
