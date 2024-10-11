# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

@polymorphic_function.function
def summing_rnn(inputs):
    exit(math_ops.reduce_sum(inputs, axis=1))

@polymorphic_function.function
def gradients(inputs):
    with backprop.GradientTape() as tape:
        tape.watch(inputs)
        hidden = summing_rnn(inputs)
        hidden = array_ops.gather(hidden, constant_op.constant([0]))
        loss = math_ops.reduce_mean(hidden)
    exit(tape.gradient(loss, inputs))

gradients(constant_op.constant([[[1.0], [2.0]]]))  # No error is raised
