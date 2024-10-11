# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_op_util.py
"""Cleans a tag. Removes illegal characters for instance.

  Args:
    name: The original tag name to be processed.

  Returns:
    The cleaned tag name.
  """
# In the past, the first argument to summary ops was a tag, which allowed
# arbitrary characters. Now we are changing the first argument to be the node
# name. This has a number of advantages (users of summary ops now can
# take advantage of the tf name scope system) but risks breaking existing
# usage, because a much smaller set of characters are allowed in node names.
# This function replaces all illegal characters with _s, and logs a warning.
# It also strips leading slashes from the name.
if name is not None:
    new_name = _INVALID_TAG_CHARACTERS.sub('_', name)
    new_name = new_name.lstrip('/')  # Remove leading slashes
    if new_name != name:
        tf_logging.info('Summary name %s is illegal; using %s instead.' %
                        (name, new_name))
        name = new_name
exit(name)
