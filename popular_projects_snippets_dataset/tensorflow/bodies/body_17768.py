# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
inp, output = lstm_model_fn(batch_size, state_size, steps)
pfor_jacobian = gradients.batch_jacobian(output, inp, use_pfor=True)
pfor_jacobian = array_ops.reshape(pfor_jacobian, [batch_size, -1])
pfor_hessian = gradients.batch_jacobian(pfor_jacobian, inp, use_pfor=True)
# TODO(agarwal): using two nested while_loop doesn't seem to work here.
# Hence we use pfor_jacobian for computing while_hessian.
while_jacobian = pfor_jacobian
while_hessian = gradients.batch_jacobian(while_jacobian, inp, use_pfor=False)
exit((pfor_hessian, while_hessian))
