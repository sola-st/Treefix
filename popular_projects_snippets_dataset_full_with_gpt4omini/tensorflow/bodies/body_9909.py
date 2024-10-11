# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Adds this import to module_imports.

    Args:
      symbol: TensorFlow Python symbol.
      source_module_name: (string) Module to import from.
      source_name: (string) Name of the symbol to import.
      dest_module_name: (string) Module name to add import to.
      dest_name: (string) Import the symbol using this name.

    Raises:
      SymbolExposedTwiceError: Raised when an import with the same
        dest_name has already been added to dest_module_name.
    """
# modules_with_exports.py is only used during API generation and
# won't be available when actually importing tensorflow.
if source_module_name.endswith('python.modules_with_exports'):
    source_module_name = symbol.__module__
import_str = self.format_import(source_module_name, source_name, dest_name)

# Check if we are trying to expose two different symbols with same name.
full_api_name = dest_name
if dest_module_name:
    full_api_name = dest_module_name + '.' + full_api_name
symbol_id = -1 if not symbol else id(symbol)
self._check_already_imported(symbol_id, full_api_name)

if not dest_module_name and dest_name.startswith('_'):
    self._underscore_names_in_root.add(dest_name)

# The same symbol can be available in multiple modules.
# We store all possible ways of importing this symbol and later pick just
# one.
priority = 0
if symbol:
    # Give higher priority to source module if it matches
    # symbol's original module.
    if hasattr(symbol, '__module__'):
        priority = int(source_module_name == symbol.__module__)
    # Give higher priority if symbol name matches its __name__.
    if hasattr(symbol, '__name__'):
        priority += int(source_name == symbol.__name__)
self._module_imports[dest_module_name][full_api_name].add(
    (import_str, priority))
