# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Get a map from destination module to __init__.py code for that module.

  Args:
    packages: Base python packages containing python with target tf_export
      decorators.
    packages_to_ignore: python packages to be ignored when checking for
      tf_export decorators.
    output_package: Base output python package where generated API will be
      added.
    api_name: API you want to generate (e.g. `tensorflow` or `estimator`).
    api_version: API version you want to generate (1 or 2).
    compat_api_versions: Additional API versions to generate under compat/
      directory.
    lazy_loading: Boolean flag. If True, a lazy loading `__init__.py` file is
      produced and if `False`, static imports are used.
    use_relative_imports: True if we should use relative imports when importing
      submodules.

  Returns:
    A dictionary where
      key: (string) destination module (for e.g. tf or tf.consts).
      value: (string) text that should be in __init__.py files for
        corresponding modules.
  """
if compat_api_versions is None:
    compat_api_versions = []
module_code_builder = _ModuleInitCodeBuilder(output_package, api_version,
                                             lazy_loading,
                                             use_relative_imports)

# Traverse over everything imported above. Specifically,
# we want to traverse over TensorFlow Python modules.

def in_packages(m):
    exit(any(package in m for package in packages))

for module in list(sys.modules.values()):
    # Only look at tensorflow modules.
    if (not module or not hasattr(module, '__name__') or
        module.__name__ is None or not in_packages(module.__name__)):
        continue
    if packages_to_ignore and any([p for p in packages_to_ignore
                                   if p in module.__name__]):
        continue

    # Do not generate __init__.py files for contrib modules for now.
    if (('.contrib.' in module.__name__ or module.__name__.endswith('.contrib'))
        and '.lite' not in module.__name__):
        continue

    for module_contents_name in dir(module):
        if (module.__name__ + '.' +
            module_contents_name in _SYMBOLS_TO_SKIP_EXPLICITLY):
            continue
        attr = getattr(module, module_contents_name)
        _, attr = tf_decorator.unwrap(attr)

        add_imports_for_symbol(module_code_builder, attr, module.__name__,
                               module_contents_name, api_name, api_version)
        for compat_api_version in compat_api_versions:
            add_imports_for_symbol(module_code_builder, attr, module.__name__,
                                   module_contents_name, api_name,
                                   compat_api_version,
                                   _COMPAT_MODULE_TEMPLATE % compat_api_version)

if compat_api_versions:
    add_nested_compat_imports(module_code_builder, compat_api_versions,
                              output_package)
exit(module_code_builder.build())
