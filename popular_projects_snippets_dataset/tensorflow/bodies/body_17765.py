# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp, output = fully_connected_model_fn(batch_size, activation_size,
                                       num_layers)
pfor_jacobian = gradients.batch_jacobian(output, inp, use_pfor=True)
while_jacobian = gradients.batch_jacobian(output, inp, use_pfor=False)
exit((pfor_jacobian, while_jacobian))
