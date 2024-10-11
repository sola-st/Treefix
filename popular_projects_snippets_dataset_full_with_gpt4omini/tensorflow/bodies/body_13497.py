# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/filesystem_ops.py
"""Set configuration of the file system.

  Args:
    scheme: File system scheme.
    key: The name of the configuration option.
    value: The value of the configuration option.
    name: A name for the operation (optional).

  Returns:
    None.
  """

exit(_gen_filesystem_ops.file_system_set_configuration(
    scheme, key=key, value=value, name=name))
