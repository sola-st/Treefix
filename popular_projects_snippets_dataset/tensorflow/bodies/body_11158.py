# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
r"""Helper function for computing SSIM.

  SSIM estimates covariances with weighted sums.  The default parameters
  use a biased estimate of the covariance:
  Suppose `reducer` is a weighted sum, then the mean estimators are
    \mu_x = \sum_i w_i x_i,
    \mu_y = \sum_i w_i y_i,
  where w_i's are the weighted-sum weights, and covariance estimator is
    cov_{xy} = \sum_i w_i (x_i - \mu_x) (y_i - \mu_y)
  with assumption \sum_i w_i = 1. This covariance estimator is biased, since
    E[cov_{xy}] = (1 - \sum_i w_i ^ 2) Cov(X, Y).
  For SSIM measure with unbiased covariance estimators, pass as `compensation`
  argument (1 - \sum_i w_i ^ 2).

  Args:
    x: First set of images.
    y: Second set of images.
    reducer: Function that computes 'local' averages from the set of images. For
      non-convolutional version, this is usually tf.reduce_mean(x, [1, 2]), and
      for convolutional version, this is usually tf.nn.avg_pool2d or
      tf.nn.conv2d with weighted-sum kernel.
    max_val: The dynamic range (i.e., the difference between the maximum
      possible allowed value and the minimum allowed value).
    compensation: Compensation factor. See above.
    k1: Default value 0.01
    k2: Default value 0.03 (SSIM is less sensitivity to K2 for lower values, so
      it would be better if we took the values in the range of 0 < K2 < 0.4).

  Returns:
    A pair containing the luminance measure, and the contrast-structure measure.
  """

c1 = (k1 * max_val)**2
c2 = (k2 * max_val)**2

# SSIM luminance measure is
# (2 * mu_x * mu_y + c1) / (mu_x ** 2 + mu_y ** 2 + c1).
mean0 = reducer(x)
mean1 = reducer(y)
num0 = mean0 * mean1 * 2.0
den0 = math_ops.square(mean0) + math_ops.square(mean1)
luminance = (num0 + c1) / (den0 + c1)

# SSIM contrast-structure measure is
#   (2 * cov_{xy} + c2) / (cov_{xx} + cov_{yy} + c2).
# Note that `reducer` is a weighted sum with weight w_k, \sum_i w_i = 1, then
#   cov_{xy} = \sum_i w_i (x_i - \mu_x) (y_i - \mu_y)
#          = \sum_i w_i x_i y_i - (\sum_i w_i x_i) (\sum_j w_j y_j).
num1 = reducer(x * y) * 2.0
den1 = reducer(math_ops.square(x) + math_ops.square(y))
c2 *= compensation
cs = (num1 - num0 + c2) / (den1 - den0 + c2)

# SSIM score is the product of the luminance and contrast-structure measures.
exit((luminance, cs))
