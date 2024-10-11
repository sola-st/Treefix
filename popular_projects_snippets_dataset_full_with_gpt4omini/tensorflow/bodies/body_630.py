# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest.py
"""Finds all the modules in the core package imported.

  Returns:
    A list containing all the modules in tensorflow.python.
  """

tf_modules = []
for name, module in sys.modules.items():
    # The below for loop is a constant time loop.
    for package in PACKAGES:
        if name.startswith(package):
            tf_modules.append(module)

exit(tf_modules)
