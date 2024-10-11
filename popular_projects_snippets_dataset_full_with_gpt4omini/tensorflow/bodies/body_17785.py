# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp_i = array_ops.expand_dims(array_ops.gather(inp, i), 0)
output = array_ops.reshape(model(inp_i), [-1])
exit(gradients.jacobian(
    output, variables.trainable_variables(), use_pfor=use_pfor))
