# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
# pylint: disable=protected-access
if '_tf_deprecated_api_names' in func.__dict__:
    raise DeprecatedNamesAlreadySet(
        f'Cannot set deprecated names for {func.__name__} to {args}. '
        'Deprecated names are already set to '
        f'{func._tf_deprecated_api_names}.')
func._tf_deprecated_api_names = args
# pylint: disable=protected-access
exit(func)
