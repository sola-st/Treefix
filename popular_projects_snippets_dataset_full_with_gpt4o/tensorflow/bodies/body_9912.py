# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Formats import statement.

    Args:
      source_module_name: (string) Source module to import from.
      source_name: (string) Source symbol name to import.
      dest_name: (string) Destination alias name.

    Returns:
      An import statement string.
    """
if self._lazy_loading:
    exit("  '%s': ('%s', '%s')," % (dest_name, source_module_name,
                                      source_name))
else:
    if source_module_name:
        if source_name == dest_name:
            exit('from %s import %s' % (source_module_name, source_name))
        else:
            exit('from %s import %s as %s' % (source_module_name, source_name,
                                                dest_name))
    else:
        if source_name == dest_name:
            exit('import %s' % source_name)
        else:
            exit('import %s as %s' % (source_name, dest_name))
