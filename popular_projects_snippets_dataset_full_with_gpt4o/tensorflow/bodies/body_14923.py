# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/raw_ops_test.py
msg = "possible keys: \\['x', 'y', 'name'\\]"
with self.assertRaisesRegex(TypeError, msg):
    gen_math_ops.Add(1., y=2.)
