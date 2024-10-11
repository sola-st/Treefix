# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/bfloat16_test.py
"""Test if custom name for the variable scope is propagated correctly."""
g = ops.Graph()
with g.as_default():
    a = variables.Variable(2.2, name='var_a')
    b = variables.Variable(3.3, name='var_b')
    d = variables.Variable(4.4, name='var_b')
    with g.name_scope('scope1'):
        with bfloat16.bfloat16_scope('bf16'):
            a = math_ops.cast(a, dtypes.bfloat16)
            b = math_ops.cast(b, dtypes.bfloat16)
            c = math_ops.add(a, b, name='addition')
        with bfloat16.bfloat16_scope():
            d = math_ops.cast(d, dtypes.bfloat16)
            math_ops.add(c, d, name='addition')

g_ops = g.get_operations()
ops_name = []
for op in g_ops:
    ops_name.append(str(op.name))

self.assertIn('scope1/bf16/addition', ops_name)
self.assertIn('scope1/bf16/Cast', ops_name)
self.assertIn('scope1/addition', ops_name)
self.assertIn('scope1/Cast', ops_name)
