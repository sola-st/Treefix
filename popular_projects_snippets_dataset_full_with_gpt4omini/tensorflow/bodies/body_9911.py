# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Get a map from destination module to __init__.py code for that module.

    Returns:
      A dictionary where
        key: (string) destination module (for e.g. tf or tf.consts).
        value: (string) text that should be in __init__.py files for
          corresponding modules.
    """
self._import_submodules()
module_text_map = {}
footer_text_map = {}
for dest_module, dest_name_to_imports in self._module_imports.items():
    # Sort all possible imports for a symbol and pick the first one.
    imports_list = [
        get_canonical_import(imports)
        for _, imports in dest_name_to_imports.items()
    ]
    if self._lazy_loading:
        module_text_map[
            dest_module] = _LAZY_LOADING_MODULE_TEXT_TEMPLATE % '\n'.join(
                sorted(imports_list))
    else:
        module_text_map[dest_module] = '\n'.join(sorted(imports_list))

    # Expose exported symbols with underscores in root module since we import
    # from it using * import. Don't need this for lazy_loading because the
    # underscore symbols are already included in __all__ when passed in and
    # handled by TFModuleWrapper.
root_module_footer = ''
if not self._lazy_loading:
    underscore_names_str = ', '.join(
        '\'%s\'' % name for name in sorted(self._underscore_names_in_root))

    root_module_footer = """
_names_with_underscore = [%s]
__all__ = [_s for _s in dir() if not _s.startswith('_')]
__all__.extend([_s for _s in _names_with_underscore])
""" % underscore_names_str

# Add module wrapper if we need to print deprecation messages
# or if we use lazy loading.
if self._api_version == 1 or self._lazy_loading:
    for dest_module, _ in self._module_imports.items():
        deprecation = 'False'
        has_lite = 'False'
        if self._api_version == 1:  # Add 1.* deprecations.
            if not dest_module.startswith(_COMPAT_MODULE_PREFIX):
                deprecation = 'True'
        # Workaround to make sure not load lite from lite/__init__.py
        if (not dest_module and 'lite' in self._module_imports and
            self._lazy_loading):
            has_lite = 'True'
        if self._lazy_loading:
            public_apis_name = '_PUBLIC_APIS'
        else:
            public_apis_name = 'None'
        footer_text_map[dest_module] = _DEPRECATION_FOOTER % (
            dest_module, public_apis_name, deprecation, has_lite)

exit((module_text_map, footer_text_map, root_module_footer))
