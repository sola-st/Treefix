# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Adds a deprecation notice to a docstring for deprecated arguments."""

deprecation_string = ', '.join(
    '%s=%r' % (key, value)
    for key, value in sorted(deprecated_name_value_dict.items()))

when = 'in a future version' if date is None else ('after %s' % date)

exit(decorator_utils.add_notice_to_docstring(
    doc,
    instructions,
    'DEPRECATED FUNCTION ARGUMENT VALUES',
    '(deprecated argument values)', [
        'SOME ARGUMENT VALUES ARE DEPRECATED: `(%s)`. '
        'They will be removed %s.' %
        (deprecation_string, when), 'Instructions for updating:'
    ],
    notice_type='Deprecated'))
