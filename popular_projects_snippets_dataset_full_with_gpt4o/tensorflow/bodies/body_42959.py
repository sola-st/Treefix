# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
if name.startswith('_tfmw_'):
    super(TFModuleWrapper, self).__delattr__(name)
else:
    delattr(self._tfmw_wrapped_module, name)
