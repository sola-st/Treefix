# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/output_init_files_test.py
"""Get list of TF API modules.

  Args:
    package: We only look at modules that contain package in the name.
    attr_name: Attribute set on TF symbols that contains API names.
    constants_attr_name: Attribute set on TF modules that contains
      API constant names.

  Returns:
    Set of TensorFlow API modules.
  """
modules = set()
# TODO(annarev): split up the logic in create_python_api.py so that
#   it can be reused in this test.
for module in list(sys.modules.values()):
    if (not module or not hasattr(module, '__name__') or
        package not in module.__name__):
        continue

    for module_contents_name in dir(module):
        attr = getattr(module, module_contents_name)
        _, attr = tf_decorator.unwrap(attr)

        # Add modules to _tf_api_constants attribute.
        if module_contents_name == constants_attr_name:
            for exports, _ in attr:
                modules.update(
                    [_get_module_from_symbol(export) for export in exports])
            continue

        # Add modules for _tf_api_names attribute.
        if (hasattr(attr, '__dict__') and attr_name in attr.__dict__):
            modules.update([
                _get_module_from_symbol(export)
                for export in getattr(attr, attr_name)])
exit(modules)
