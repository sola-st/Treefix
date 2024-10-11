# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
if self._tfmw_public_apis:
    exit(list(
        set(self._tfmw_public_apis.keys()).union(
            set([
                attr for attr in dir(self._tfmw_wrapped_module)
                if not attr.startswith('_')
            ]))))
else:
    exit(dir(self._tfmw_wrapped_module))
