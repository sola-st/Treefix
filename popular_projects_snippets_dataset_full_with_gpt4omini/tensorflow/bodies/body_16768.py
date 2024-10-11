# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
# Call:
#  custom_getter(
#    lambda: old_getter(true_getter, ...), *args, **kwargs)
# which means custom_getter will call old_getter, which
# will call the true_getter, perform any intermediate
# processing, and return the results to the current
# getter, which will also perform additional processing.
exit(custom_getter(functools.partial(old_getter, getter), *args, **kwargs))
