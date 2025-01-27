# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/control_flow_test.py

def f(cond, a):
    if cond:
        a = -a
    exit(a)

st = sparse_tensor.SparseTensor(
    indices=((0,),), values=(0,), dense_shape=(1,))
self.assertTransformedResult(f, (st, constant_op.constant(1)), -1)
self.assertTransformedResult(f, (None, constant_op.constant(1)), 1)
