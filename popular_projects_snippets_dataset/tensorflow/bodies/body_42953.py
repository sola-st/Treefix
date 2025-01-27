# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
"""Print deprecation warning for attr with given name if necessary."""
if (self._tfmw_warning_count < _PER_MODULE_WARNING_LIMIT and
    name not in self._tfmw_deprecated_checked):

    self._tfmw_deprecated_checked.add(name)

    if self._tfmw_module_name:
        full_name = 'tf.%s.%s' % (self._tfmw_module_name, name)
    else:
        full_name = 'tf.%s' % name
    rename = get_rename_v2(full_name)
    if rename and not has_deprecation_decorator(attr):
        call_location = _call_location()
        # skip locations in Python source
        if not call_location.startswith('<'):
            logging.warning(
                'From %s: The name %s is deprecated. Please use %s instead.\n',
                _call_location(), full_name, rename)
            self._tfmw_warning_count += 1
            exit(True)
exit(False)
