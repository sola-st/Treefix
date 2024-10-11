# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp, (_, final_state) = dynamic_lstm_model_fn(batch_size, state_size,
                                              max_steps)
pfor_jacobian = gradients.batch_jacobian(final_state.c, inp, use_pfor=True)
# Note that use_pfor=False does not work above given the current limitations
# on implementation of while_loop. So we statically unroll the looping in the
# jacobian computation.
while_gradients = [
    gradient_ops.gradients(array_ops.gather(final_state.c, i, axis=1), inp)[0]
    for i in range(state_size)
]
exit((pfor_jacobian, while_gradients))
