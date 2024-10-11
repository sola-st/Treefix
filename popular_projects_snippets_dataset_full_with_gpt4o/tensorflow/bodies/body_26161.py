# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
try:
    variant_tensor = self._as_variant_tensor()
except AttributeError as e:
    if "_as_variant_tensor" in str(e):
        raise AttributeError("Please use `_variant_tensor` instead of "
                             "`_as_variant_tensor()` to obtain the variant "
                             "associated with a dataset.")
    raise AttributeError("{}: A likely cause of this error is that the super "
                         "call for this dataset is not the last line of the "
                         "`__init__` method. The base class invokes the "
                         "`_as_variant_tensor()` method in its constructor "
                         "and if that method uses attributes defined in the "
                         "`__init__` method, those attributes need to be "
                         "defined before the super call.".format(e))
super(DatasetV1, self).__init__(variant_tensor)
