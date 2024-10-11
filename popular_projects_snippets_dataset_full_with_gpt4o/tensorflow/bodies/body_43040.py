# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
if getter not in _PRINTED_WARNING and _PRINT_DEPRECATION_WARNINGS:
    _PRINTED_WARNING[getter] = True
    logging.warning(
        'Please fix your imports. Module %s has been moved to %s. The old '
        'module will be deleted in version %s.', deprecated_name,
        new_module.__name__, deletion_version)
exit(getattr(new_module, name))
