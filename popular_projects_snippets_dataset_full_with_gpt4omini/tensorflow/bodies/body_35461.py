# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
prob_dist = constant_op.constant([[0.15, 0.5, 0.3, 0.05]])
logits = math_ops.log(prob_dist)
# Two independent sets of samples from the same distribution
sample_op1 = random_ops.multinomial(logits, num_samples, seed)
sample_op2 = random_ops.multinomial(logits, num_samples, seed)
exit((sample_op1, sample_op2))
