# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a Jax serving func based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ImportError:
        If cannot import the xla_computation from jax.
      ValueError:
        No serving function is specified.
        Input tensors are not specified.
        The truth value of an array with more than one element is ambiguous.
        Failed to convert the given Jax function to hlo.

    """
if not _xla_computation:
    raise ImportError("Cannot import xla_computation from jax.")

if not self._serving_funcs:
    raise ValueError("No serving func is specified.")

if not self._inputs:
    raise ValueError("Input tensors are not specified.")

if len(self._inputs) != len(self._serving_funcs):
    msg = ("Input tensor mapping len {} does not match serving func len {}."
           .format(len(self._inputs), len(self._serving_funcs)))
    raise ValueError(msg)

if not isinstance(self._inputs, (tuple, list)):
    raise ValueError(
        "Input tensors should be pass in a tuple list wrapped in an array.")

# TODO(b/197690428): Support multiple functions.
# Currently only support one serving function.
if len(self._serving_funcs) > 1:
    raise ValueError("Currently only support single serving function.")

if not isinstance(self._inputs[0], (tuple, list)):
    raise ValueError("The input placeholders are not a dictionary.")

input_names = []
ordered_inputs = []
for input_name, tensor in self._inputs[0]:
    input_names.append(input_name)
    ordered_inputs.append(tensor)

try:
    xla_compuation = _xla_computation(self._serving_funcs[0], backend="cpu")
    hlo_proto = xla_compuation(
        *ordered_inputs).as_serialized_hlo_module_proto()
except Exception:  # pylint: disable=broad-except
    raise ValueError("Failed to convert the given Jax function to hlo.")

# We need to set the hlo proto, and here we use serialized proto format
# since it's more compact.
converter_kwargs = {
    "input_content": hlo_proto,
    "input_names": input_names,
    "is_proto_format": True
}
converter_kwargs.update(self._get_base_converter_args())

# Get quantization options and do some checks.
quant_mode = QuantizationMode(self.optimizations, self.target_spec,
                              self.representative_dataset, None)
self._validate_inference_input_output_types(quant_mode)
converter_kwargs.update(quant_mode.converter_flags())
result = _convert_jax_hlo(**converter_kwargs)

exit(self._optimize_tflite_model(
    result, quant_mode, quant_io=self.experimental_new_quantizer))
