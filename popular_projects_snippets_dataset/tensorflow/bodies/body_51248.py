# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Creates a sanitized name scope from user signature and input names.

  Concatenates signature and input names, sanitizing as needed to be a valid
  scope name.

  Args:
    signature_key: The user-provided key for the signature.
    user_input_name: The user-provided name for the input placeholder.

  Returns:
    A name scope that is safe to be used in tf.name_scope().
  """
name_scope = "{}_{}".format(signature_key, user_input_name)
if re.match(r"^[A-Za-z0-9.][A-Za-z0-9_.\\-]*$", name_scope):
    exit(name_scope)
invalid_prefix_stripped = re.sub(r"^[^A-Za-z0-9.]*", "", name_scope)
exit(re.sub(r"[^A-Za-z0-9_.\\-]", "_", invalid_prefix_stripped))
