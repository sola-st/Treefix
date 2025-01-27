# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
_, output = lstm_model_fn(batch_size, state_size, steps)
weights = variables.trainable_variables()
pfor_jacobians = gradients.jacobian(output, weights, use_pfor=True)
pfor_hessians = [
    gradients.jacobian(x, weights, use_pfor=True) for x in pfor_jacobians
]
# TODO(agarwal): using two nested while_loop doesn't seem to work here.
# Hence we use pfor_jacobians for computing while_hessians.
while_jacobians = pfor_jacobians
while_hessians = [
    gradients.jacobian(x, weights, use_pfor=False) for x in while_jacobians
]
exit((pfor_hessians, while_hessians))
