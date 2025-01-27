# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""He uniform variance scaling initializer.

  Initializers allow you to pre-specify an initialization strategy, encoded in
  the Initializer object, without knowing the shape and dtype of the variable
  being initialized.

  Draws samples from a uniform distribution within [-limit, limit] where `limit`
  is `sqrt(6 / fan_in)` where `fan_in` is the number of input units in the
  weight tensor.

  Examples:

  >>> def make_variables(k, initializer):
  ...   return (tf.Variable(initializer(shape=[k, k], dtype=tf.float32)),
  ...           tf.Variable(initializer(shape=[k, k, k], dtype=tf.float32)))
  >>> v1, v2 = make_variables(3, tf.initializers.he_uniform())
  >>> v1
  <tf.Variable ... shape=(3, 3) ...
  >>> v2
  <tf.Variable ... shape=(3, 3, 3) ...
  >>> make_variables(4, tf.initializers.RandomNormal())
  (<tf.Variable ... shape=(4, 4) dtype=float32...
   <tf.Variable ... shape=(4, 4, 4) dtype=float32...

  Args:
    seed: A Python integer. Used to seed the random generator.

  Returns:
    A callable Initializer with `shape` and `dtype` arguments which generates a
    tensor.

  References:
      [He et al., 2015](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper.html) # pylint: disable=line-too-long
      ([pdf](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/He_Delving_Deep_into_ICCV_2015_paper.pdf))
  """
exit(VarianceScaling(
    scale=2., mode="fan_in", distribution="uniform", seed=seed))
