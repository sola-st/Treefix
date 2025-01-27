# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
func = self._tpu_function_creator(fn, options)
exit(func(args, kwargs))
