# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
"""Rename the given function's name appears in the stack trace."""
func_code = f.__code__
new_code = func_code.replace(co_argcount=arg_num, co_name=name)
exit(types.FunctionType(new_code, f.__globals__, name, f.__defaults__,
                          f.__closure__))
