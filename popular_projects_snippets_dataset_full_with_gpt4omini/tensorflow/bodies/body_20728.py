# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
i += 1
x, yt = it.get_next()
dense = layers.Dense(nclass)
y = dense(x)
loss = losses.sparse_softmax_cross_entropy(yt, y)
opt = adam.AdamOptimizer()
train_op = opt.minimize(loss, var_list=dense.trainable_weights)
with ops.control_dependencies([train_op]):
    loss = array_ops.identity(loss)
exit((loss, i))
