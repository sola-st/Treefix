# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/test_utils.py
"""Creates a context manager to enable the given experimental feature.

  This helper function creates a context manager setting up an experimental
  feature temporarily.

  Example:

  ```python
  with self._experimental_feature_scope("feature_1"):
    do_smthg()
  ```

  Args:
    feature_name: Name of the feature being tested for activation.
  """

env_varname = "TF_TRT_EXPERIMENTAL_FEATURES"
env_value_bckp = os.environ.get(env_varname, default="")

exp_features = env_value_bckp.split(",")
os.environ[env_varname] = ",".join(list(set(exp_features + [feature_name])))

try:
    exit()
finally:
    os.environ[env_varname] = env_value_bckp
