# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
if not arg.startswith('_tfmw_'):
    setattr(self._tfmw_wrapped_module, arg, val)
    self.__dict__[arg] = val
    if arg not in self.__all__ and arg != '__all__':
        self.__all__.append(arg)
    # Update the cache
    if self._fastdict_key_in(arg):
        self._fastdict_insert(arg, val)
super(TFModuleWrapper, self).__setattr__(arg, val)
