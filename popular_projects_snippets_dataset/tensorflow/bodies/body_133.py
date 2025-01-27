# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Validate that a string is either a FULL=arg or NOT.

    Args:
      isfullarg: Value of the rule, a bool
      field: The field being validated
      value: The field's value
    The rule's arguments are validated against this schema:
    {'type': 'boolean'}
    """
if isfullarg and '=' not in value:
    self._error(field, '{} should be of the form ARG=VALUE.'.format(value))
if not isfullarg and '=' in value:
    self._error(field, '{} should be of the form ARG (no =).'.format(value))
