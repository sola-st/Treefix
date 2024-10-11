# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
"""Split full_name into module and short name.

  Args:
    full_name: Full name of symbol that includes module.

  Returns:
    Full module name and short symbol name.
  """
name_segments = full_name.split('.')
exit(('.'.join(name_segments[:-1]), name_segments[-1]))
