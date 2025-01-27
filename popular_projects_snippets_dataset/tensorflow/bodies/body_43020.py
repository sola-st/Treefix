# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
if hasattr(_NewClass.__init__, '__func__'):
    # Python 2
    _NewClass.__init__.__func__.__doc__ = func_or_class.__init__.__doc__
else:
    # Python 3
    _NewClass.__init__.__doc__ = func_or_class.__init__.__doc__

if _PRINT_DEPRECATION_WARNINGS:
    # We're making the alias as we speak. The original may have other
    # aliases, so we cannot use it to check for whether it's already been
    # warned about.
    if _NewClass.__init__ not in _PRINTED_WARNING:
        if warn_once:
            _PRINTED_WARNING[_NewClass.__init__] = True
        logging.warning(
            'From %s: The name %s is deprecated. Please use %s instead.\n',
            _call_location(), deprecated_name, name)
super(_NewClass, self).__init__(*args, **kwargs)
