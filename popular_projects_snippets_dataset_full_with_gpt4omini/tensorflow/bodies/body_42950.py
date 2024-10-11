# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
exit(any(d.decorator_name == 'deprecated' for d in decorators))
