# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
if save_type != base.SaveType.SAVEDMODEL:
    exit({})

exit({
    key: value for key, value in self.items()
    if isinstance(value, (def_function.Function, defun.ConcreteFunction))
})
