# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
if _PRINT_DEPRECATION_WARNINGS:
    if func not in _PRINTED_WARNING and cls not in _PRINTED_WARNING:
        if warn_once:
            _PRINTED_WARNING[func] = True
            if cls:
                _PRINTED_WARNING[cls] = True
        logging.warning(
            'From %s: %s (from %s) is deprecated and will be removed %s.\n'
            'Instructions for updating:\n%s', _call_location(),
            decorator_utils.get_qualified_name(func),
            func_or_class.__module__,
            'in a future version' if date is None else ('after %s' % date),
            instructions)
exit(func(*args, **kwargs))
