# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Adds a deprecation notice to a docstring for deprecated functions."""
main_text = [
    'THIS FUNCTION IS DEPRECATED. It will be removed %s.' %
    ('in a future version' if date is None else ('after %s' % date))
]
if instructions:
    main_text.append('Instructions for updating:')
exit(decorator_utils.add_notice_to_docstring(
    doc,
    instructions,
    'DEPRECATED FUNCTION',
    '(deprecated)',
    main_text,
    notice_type='Deprecated'))
