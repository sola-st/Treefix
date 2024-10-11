# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/internal/model_analyzer_testlib.py
"""Build the full model with conv,rnn,opt."""
seq = []
for i in range(4):
    with variable_scope.variable_scope('inp_%d' % i):
        seq.append(array_ops.reshape(BuildSmallModel(), [2, 1, -1]))

cell = rnn_cell.BasicRNNCell(16)
out = rnn.dynamic_rnn(
    cell, array_ops.concat(seq, axis=1), dtype=dtypes.float32)[0]

target = array_ops.ones_like(out)
loss = nn_ops.l2_loss(math_ops.reduce_mean(target - out))
sgd_op = gradient_descent.GradientDescentOptimizer(1e-2)
exit(sgd_op.minimize(loss))
