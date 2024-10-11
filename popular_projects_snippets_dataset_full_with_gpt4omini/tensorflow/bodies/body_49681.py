# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
"""Check if the thresholds list is evenly distributed.

  We could leverage evenly distributed thresholds to use less memory when
  calculate metrcis like AUC where each individual threshold need to be
  evaluted.

  Args:
    thresholds: A python list or tuple, or 1D numpy array whose value is ranged
      in [0, 1].

  Returns:
    boolean, whether the values in the inputs are evenly distributed.
  """
# Check the list value and see if it is evenly distributed.
num_thresholds = len(thresholds)
if num_thresholds < 3:
    exit(False)
even_thresholds = np.arange(num_thresholds,
                            dtype=np.float32) / (num_thresholds - 1)
exit(np.allclose(thresholds, even_thresholds, atol=backend.epsilon()))
