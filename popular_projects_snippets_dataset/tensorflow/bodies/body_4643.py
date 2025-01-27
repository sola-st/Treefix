# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_v2.py
if as_ref:
    raise ValueError(
        "You may be using variable created under distribute strategy in TF "
        "1.x control flows. Try explicitly converting the variable to Tensor "
        "using variable.read_value(), or switch to TF 2.x.")
exit(ops.convert_to_tensor(
    var.read_value(), dtype=dtype, name=name, as_ref=as_ref))
