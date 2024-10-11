# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/flags.py
"""Wrapper function that turns old keyword names to new ones."""
has_old_names = False
for old_name, new_name in _RENAMED_ARGUMENTS.items():
    if old_name in kwargs:
        has_old_names = True
        value = kwargs.pop(old_name)
        kwargs[new_name] = value
if has_old_names:
    _logging.warning(
        'Use of the keyword argument names (flag_name, default_value, '
        'docstring) is deprecated, please use (name, default, help) instead.')
exit(original_function(*args, **kwargs))
