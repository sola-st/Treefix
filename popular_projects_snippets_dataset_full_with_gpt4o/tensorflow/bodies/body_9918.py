# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Add imports for the given symbol to `module_code_builder`.

  Args:
    module_code_builder: `_ModuleInitCodeBuilder` instance.
    symbol: A symbol.
    source_module_name: Module that we can import the symbol from.
    source_name: Name we can import the symbol with.
    api_name: API name. Currently, must be either `tensorflow` or `estimator`.
    api_version: API version.
    output_module_prefix: Prefix to prepend to destination module.
  """
if api_version == 1:
    names_attr = API_ATTRS_V1[api_name].names
    constants_attr = API_ATTRS_V1[api_name].constants
else:
    names_attr = API_ATTRS[api_name].names
    constants_attr = API_ATTRS[api_name].constants

# If symbol is _tf_api_constants attribute, then add the constants.
if source_name == constants_attr:
    for exports, name in symbol:
        for export in exports:
            dest_module, dest_name = _get_name_and_module(export)
            dest_module = _join_modules(output_module_prefix, dest_module)
            module_code_builder.add_import(None, source_module_name, name,
                                           dest_module, dest_name)

  # If symbol has _tf_api_names attribute, then add import for it.
if (hasattr(symbol, '__dict__') and names_attr in symbol.__dict__):

    # Generate import statements for symbols.
    for export in getattr(symbol, names_attr):  # pylint: disable=protected-access
        dest_module, dest_name = _get_name_and_module(export)
        dest_module = _join_modules(output_module_prefix, dest_module)
        module_code_builder.add_import(symbol, source_module_name, source_name,
                                       dest_module, dest_name)
