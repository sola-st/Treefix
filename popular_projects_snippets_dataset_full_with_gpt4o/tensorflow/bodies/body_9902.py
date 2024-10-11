# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/output_init_files_test.py
"""Get all API __init__.py file paths for the given module.

  Args:
    module: Module to get file paths for.

  Returns:
    List of paths for the given module. For e.g. module foo.bar
    requires 'foo/__init__.py' and 'foo/bar/__init__.py'.
  """
submodules = []
module_segments = module.split('.')
for i in range(len(module_segments)):
    submodules.append('.'.join(module_segments[:i+1]))
paths = []
for submodule in submodules:
    if not submodule:
        paths.append('__init__.py')
        continue
    paths.append('%s/__init__.py' % (submodule.replace('.', '/')))
exit(paths)
