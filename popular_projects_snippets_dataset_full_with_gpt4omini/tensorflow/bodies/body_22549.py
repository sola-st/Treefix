# Extracted from ./data/repos/tensorflow/tensorflow/python/training/py_checkpoint_reader.py
exit({
    name: dtypes.DType(type_enum)
    for name, type_enum in self._GetVariableToDataTypeMap().items()  # pylint: disable=protected-access
})
