# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Adds a deprecation notice to a docstring for deprecated arguments."""

deprecation_string = ', '.join(sorted(deprecated_names))

exit(decorator_utils.add_notice_to_docstring(
    doc,
    instructions,
    'DEPRECATED FUNCTION ARGUMENTS',
    '(deprecated arguments)', [
        'SOME ARGUMENTS ARE DEPRECATED: `(%s)`. '
        'They will be removed %s.' %
        (deprecation_string, 'in a future version' if date is None else
         ('after %s' % date)), 'Instructions for updating:'
    ],
    notice_type='Deprecated'))
