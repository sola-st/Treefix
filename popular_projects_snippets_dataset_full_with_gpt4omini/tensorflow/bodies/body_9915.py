# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Adds compat.vN.compat.vK modules to module builder.

  To avoid circular imports, we want to add __init__.py files under
  compat.vN.compat.vK and under compat.vN.compat.vK.compat. For all other
  imports, we point to corresponding modules under compat.vK.

  Args:
    module_builder: `_ModuleInitCodeBuilder` instance.
    compat_api_versions: Supported compatibility versions.
    output_package: Base output python package where generated API will be
      added.
  """
imported_modules = module_builder.get_destination_modules()

# Copy over all imports in compat.vK to compat.vN.compat.vK and
# all imports in compat.vK.compat to compat.vN.compat.vK.compat.
for v in compat_api_versions:
    for sv in compat_api_versions:
        subcompat_module = _SUBCOMPAT_MODULE_TEMPLATE % (v, sv)
        compat_module = _COMPAT_MODULE_TEMPLATE % sv
        module_builder.copy_imports(compat_module, subcompat_module)
        module_builder.copy_imports('%s.compat' % compat_module,
                                    '%s.compat' % subcompat_module)

  # Prefixes of modules under compatibility packages, for e.g. "compat.v1.".
compat_prefixes = tuple(
    _COMPAT_MODULE_TEMPLATE % v + '.' for v in compat_api_versions)

# Above, we only copied function, class and constant imports. Here
# we also add imports for child modules.
for imported_module in imported_modules:
    if not imported_module.startswith(compat_prefixes):
        continue
    module_split = imported_module.split('.')

    # Handle compat.vN.compat.vK.compat.foo case. That is,
    # import compat.vK.compat.foo in compat.vN.compat.vK.compat.
    if len(module_split) > 3 and module_split[2] == 'compat':
        src_module = '.'.join(module_split[:3])
        src_name = module_split[3]
        assert src_name != 'v1' and src_name != 'v2', imported_module
    else:  # Handle compat.vN.compat.vK.foo case.
        src_module = '.'.join(module_split[:2])
        src_name = module_split[2]
        if src_name == 'compat':
            continue  # compat.vN.compat.vK.compat is handled separately

    for compat_api_version in compat_api_versions:
        module_builder.add_import(
            symbol=None,
            source_module_name='%s.%s' % (output_package, src_module),
            source_name=src_name,
            dest_module_name='compat.v%d.%s' % (compat_api_version, src_module),
            dest_name=src_name)
