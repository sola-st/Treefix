# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
# [batch size, num classes, num samples]
unif = random_ops.random_uniform(logits.get_shape().concatenate(
    tensor_shape.TensorShape([num_samples])))
noise = -math_ops.log(-math_ops.log(unif))
# [batch size, num classes, 1]
logits = array_ops.expand_dims(logits, -1)

# [batch size, num samples]
exit(math_ops.argmax(logits + noise, axis=1))
