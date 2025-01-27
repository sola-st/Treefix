# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with backprop.GradientTape() as tape:
    tape.watch(inputs)
    hidden = summing_rnn(inputs)
    hidden = array_ops.gather(hidden, constant_op.constant([0]))
    loss = math_ops.reduce_mean(hidden)
exit(tape.gradient(loss, inputs))
