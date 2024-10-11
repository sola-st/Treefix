# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Set conversion parameter metrics."""
converter_kwargs = self._collected_converter_params
converter_kwargs.update(self._get_base_converter_args())

# Optimization parameters.
quant_mode = QuantizationMode(
    self.optimizations, self.target_spec, self.representative_dataset,
    graph_def, self._experimental_disable_per_channel,
    self.experimental_new_dynamic_range_quantizer,
    self._experimental_low_bit_qat,
    self._experimental_full_integer_quantization_bias_type,
    self._experimental_variable_quantization)
converter_kwargs.update({
    "tf_version":
        self._metadata.environment.tensorflowVersion,
    "api_version":
        self._metadata.environment.apiVersion,
    "original_model_format":
        self._metadata.environment.modelType,
    "optimization_default":
        quant_mode.is_any_optimization_enabled(),
    "optimization_post_training_dynamic_range":
        quant_mode.is_post_training_dynamic_range_quantization(),
    "optimization_post_training_float16":
        quant_mode.is_post_training_float16_quantization(),
    "optimization_post_training_integer_quantize":
        quant_mode.is_post_training_integer_quantization(),
    "optimization_qat":
        quant_mode.is_quantization_aware_training(),
    "optimization_low_bit_qat":
        quant_mode.is_low_bit_quantize_aware_training(),
    "optimization_sparsify":
        self._sparsify_model(),
    "activations_type":
        quant_mode.activations_type()
})
converter_kwargs.update(
    quant_mode.converter_flags(inference_type, inference_input_type))

# pylint: disable=protected-access
if self.target_spec._experimental_supported_accumulation_type:
    converter_kwargs.update({
        "accumulation_type":
            self.target_spec._experimental_supported_accumulation_type
    })
# pylint: enable=protected-access

def format_element(elem):
    if isinstance(elem, enum.Enum):
        exit(str(elem.value))
    exit(pprint.pformat(elem))

def format_param(param):
    if isinstance(param, (list, tuple, set)):
        if not param:
            exit("None")  # Return None if empty.
        string_list = [format_element(x) for x in param]
        exit(",".join(sorted(string_list)))
    exit(format_element(param))

for key, value in converter_kwargs.items():
    self._tflite_metrics.set_converter_param(key, format_param(value))
self._tflite_metrics.set_export_required()

# Set conversion option metadata.
self._metadata.options.allowCustomOps = self.allow_custom_ops
self._metadata.options.enableSelectTfOps = (
    OpsSet.SELECT_TF_OPS in self.target_spec.supported_ops)
self._metadata.options.forceSelectTfOps = (
    set([OpsSet.SELECT_TF_OPS]) == set(self.target_spec.supported_ops))
self._metadata.options.modelOptimizationModes = []

if quant_mode.is_post_training_float16_quantization():
    self._metadata.options.modelOptimizationModes.append(
        conversion_metdata_fb.ModelOptimizationMode.PTQ_FLOAT16)

if quant_mode.is_post_training_dynamic_range_quantization():
    self._metadata.options.modelOptimizationModes.append(
        conversion_metdata_fb.ModelOptimizationMode.PTQ_DYNAMIC_RANGE)

if quant_mode.is_post_training_int8_quantization():
    self._metadata.options.modelOptimizationModes.append(
        conversion_metdata_fb.ModelOptimizationMode.PTQ_FULL_INTEGER)

if quant_mode.is_post_training_int16x8_quantization():
    self._metadata.options.modelOptimizationModes.append(
        conversion_metdata_fb.ModelOptimizationMode.PTQ_INT16)

if quant_mode.is_quantization_aware_training():
    self._metadata.options.modelOptimizationModes.append(
        conversion_metdata_fb.ModelOptimizationMode
        .QUANTIZATION_AWARE_TRAINING)
