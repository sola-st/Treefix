# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
self._device_name_or_function = device_name_or_function
self.display_name = str(self._device_name_or_function)
self.function = device_name_or_function
self.raw_string = None

if isinstance(device_name_or_function, pydev.MergeDevice):
    self.is_null_merge = device_name_or_function.is_null_merge

elif callable(device_name_or_function):
    self.is_null_merge = False
    dev_func = self._device_name_or_function
    func_name = function_utils.get_func_name(dev_func)
    func_code = function_utils.get_func_code(dev_func)
    if func_code:
        fname = func_code.co_filename
        lineno = func_code.co_firstlineno
    else:
        fname = "unknown"
        lineno = -1
    self.display_name = "%s<%s, %d>" % (func_name, fname, lineno)

elif device_name_or_function is None:
    # NOTE(taylorrobie): This MUST be False. None signals a break in the
    #   device stack, so `is_null_merge` must be False for such a case to
    #   allow callers to safely skip over null merges without missing a None.
    self.is_null_merge = False

else:
    self.raw_string = device_name_or_function
    self.function = pydev.merge_device(device_name_or_function)
    self.is_null_merge = self.function.is_null_merge

# We perform this check in __init__ because it is of non-trivial cost,
# and self.string_merge is typically called many times.
self.fast_string_merge = isinstance(self.function, pydev.MergeDevice)
