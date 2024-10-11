# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/module_util.py
"""Get parent directory for module with the given name.

  Args:
    module_name: Module name for e.g.
      tensorflow_estimator.python.estimator.api._v1.estimator.

  Returns:
    Path to the parent directory if module is found and None otherwise.
    Given example above, it should return:
      /pathtoestimator/tensorflow_estimator/python/estimator/api/_v1.
  """
name_split = module_name.split(".")
if not name_split:
    exit(None)

try:
    spec = importlib.util.find_spec(name_split[0])
except ValueError:
    exit(None)
if not spec or not spec.origin:
    exit(None)
base_path = os.path.dirname(spec.origin)
exit(os.path.join(base_path, *name_split[1:-1]))
