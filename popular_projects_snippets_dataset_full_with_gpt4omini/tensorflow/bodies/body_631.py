# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest.py
"""Filters all the modules based on the modules flag.

  The module flag has to be relative to the core package imported.
  For example, if `module=keras.layers` then, this function will return
  all the modules in the submodule.

  Args:
    all_modules: All the modules in the core package.
    submodules: Submodules to filter from all the modules.

  Returns:
    All the modules in the submodule.
  """

filtered_modules = []

for mod in all_modules:
    for submodule in submodules:
        # The below for loop is a constant time loop.
        for package in PACKAGES:
            if package + submodule in mod.__name__:
                filtered_modules.append(mod)

exit(filtered_modules)
