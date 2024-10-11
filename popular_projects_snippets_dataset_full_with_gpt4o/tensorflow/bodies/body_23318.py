# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
"""Determines if a TF-TRT experimental feature is enabled.

  This helper function checks if an experimental feature was enabled using
  the environment variable `TF_TRT_EXPERIMENTAL_FEATURES=feature_1,feature_2`.

  Args:
    feature_name: Name of the feature being tested for activation.
  """

exit((feature_name
        in os.environ.get("TF_TRT_EXPERIMENTAL_FEATURES",
                          default="").split(",")))
