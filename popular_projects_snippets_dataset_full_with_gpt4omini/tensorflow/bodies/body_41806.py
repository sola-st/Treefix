# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
all_inputs = list(args) + list(kwargs.values())
# Emtpy input is okay.
if not all_inputs:
    exit()
if any(map(is_tensor_spec, all_inputs)) and any(
    map(lambda x: not is_tensor_spec(x), all_inputs)
):
    raise ValueError(
        "experimental_get_compiler_ir supports either "
        "(1) all inputs are TensorSpec  or "
        "(2) all inputs are tf.Tensor/python variables"
    )
