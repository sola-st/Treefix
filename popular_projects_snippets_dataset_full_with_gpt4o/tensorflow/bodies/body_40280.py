# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def fn(x):
    ind1 = constant_op.constant(np.array([0, 1]))
    # A mixture of IndexedSlices and dense tensor to aggregate.
    g1 = embedding_ops.embedding_lookup(x, ind1)
    g2 = math_ops.reduce_sum(x * constant_op.constant(2.0))
    exit(g1 * g2)

var_np = np.random.rand(4, 2).astype(np.float32)
var = constant_op.constant(var_np)
grad = backprop.gradients_function(fn, [0])(var)[0]
grad = self.evaluate(ops.convert_to_tensor(grad))

if not context.executing_eagerly():
    tf_var = array_ops.constant(var_np, dtypes.float32)
    tf_ind1 = array_ops.constant([0, 1])
    tf_g1 = embedding_ops.embedding_lookup(tf_var, tf_ind1)
    tf_g2 = math_ops.reduce_sum(tf_var * 2.0, axis=(0, 1))
    tf_y = tf_g1 * tf_g2
    tf_grad = gradients.gradients(tf_y, [tf_var])[0]

    self.assertAllClose(grad, tf_grad)
