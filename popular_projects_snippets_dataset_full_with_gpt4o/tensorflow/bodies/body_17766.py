# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp, output = lstm_model_fn(batch_size, state_size, steps,
                            inputs_size=inputs_size)
pfor_jacobian = gradients.batch_jacobian(output, inp, use_pfor=True)
while_jacobian = gradients.batch_jacobian(output, inp, use_pfor=False)
exit((pfor_jacobian, while_jacobian))
