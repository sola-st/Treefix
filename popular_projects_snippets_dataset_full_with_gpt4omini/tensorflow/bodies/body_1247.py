# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/gather_nd_op_test.py
with self.session():
    paramsp = array_ops.placeholder(params.dtype)
    indicesp = array_ops.placeholder(indices.dtype)
    with self.test_scope():
        gather_nd_t = array_ops.gather_nd(paramsp, indicesp)
    feed_dict = {paramsp: params, indicesp: indices}
    exit(gather_nd_t.eval(feed_dict=feed_dict))
