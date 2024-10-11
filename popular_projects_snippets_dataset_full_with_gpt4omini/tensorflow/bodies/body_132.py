# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Validate that a partial references an existing partial spec.

    Args:
      ispartial: Value of the rule, a bool
      field: The field being validated
      value: The field's value
    The rule's arguments are validated against this schema:
    {'type': 'boolean'}
    """
if ispartial and value not in self.partials:
    self._error(field,
                '{} is not present in the partials directory.'.format(value))
