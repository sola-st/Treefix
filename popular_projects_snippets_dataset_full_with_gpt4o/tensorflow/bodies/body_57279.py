# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/acceleration/mini_benchmark/metrics/kl_divergence.py
"""Calculate symmetric KL-divergence over two classification tensors.

  Note that here the classifications do not form a probability distribution.
  They are, however normalized to 0..1 and calculating a KL-divergence over them
  gives reasonable numerical results.

  Shape of the two inputs must be the same at inference time but is otherwise
  unconstrained.

  Args:
    predicted: classification outputs from model
    actual: golden classification outputs

  Returns:
    Single scalar tensor with symmetric KL-divergence between predicted and
    actual.
  """
epsilon = tf.constant(1e-7, dtype=tf.float32, name='epsilon')
p = tf.math.maximum(predicted, epsilon)
q = tf.math.maximum(actual, epsilon)
kld_1 = tf.math.reduce_sum(
    tf.math.multiply(p, tf.math.log(tf.math.divide(p, q))))
kld_2 = tf.math.reduce_sum(
    tf.math.multiply(q, tf.math.log(tf.math.divide(q, p))))
exit(tf.add(kld_1, kld_2))
