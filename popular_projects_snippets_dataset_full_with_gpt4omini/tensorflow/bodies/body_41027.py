# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Checks args and kwargs against the specified input_signature."""
if kwargs:
    raise ValueError("Cannot define a TensorFlow function from a Python "
                     "function with keyword arguments when "
                     "input_signature is provided, got keyword arguments "
                     f"({kwargs}) with input_signature "
                     f"({self.input_signature}).")
if args:
    # If args are provided, they must match the input signature.
    input_signature_args = args[:len(self.input_signature)]
    if not is_same_structure(self.input_signature, input_signature_args):
        raise ValueError("Structure of Python function inputs does not match "
                         f"input_signature: inputs ({args}), "
                         f"input_signature ({self.input_signature}).")
    flat_inputs = nest.flatten(input_signature_args, expand_composites=True)
    if any(not isinstance(arg, (ops.Tensor, tensor_spec.DenseSpec,
                                resource_variable_ops.BaseResourceVariable))
           for arg in flat_inputs):
        raise ValueError("When input_signature is provided, all inputs to "
                         "the Python function must be Tensors, Variables, "
                         "tf.TensorSpec or tf.VariableSpec objects.")
    if any(not spec.is_compatible_with(other)
           for spec, other in zip(self.flat_input_signature, flat_inputs)):
        raise ValueError("Python inputs incompatible with input_signature: "
                         f"inputs ({args}), input_signature "
                         f"({self.input_signature}).")
