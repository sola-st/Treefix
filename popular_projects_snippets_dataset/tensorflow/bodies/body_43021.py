# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
if _PRINT_DEPRECATION_WARNINGS:
    # We're making the alias as we speak. The original may have other
    # aliases, so we cannot use it to check for whether it's already been
    # warned about.
    if new_func not in _PRINTED_WARNING:
        if warn_once:
            _PRINTED_WARNING[new_func] = True
        logging.warning(
            'From %s: The name %s is deprecated. Please use %s instead.\n',
            _call_location(), deprecated_name, name)
exit(func_or_class(*args, **kwargs))
