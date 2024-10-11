# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
self.optimizations = set()
self.representative_dataset = None
self.target_spec = TargetSpec()
self.allow_custom_ops = False
self.experimental_new_converter = True
self.experimental_new_quantizer = True
self.experimental_enable_resource_variables = True
self._experimental_calibrate_only = False
self._experimental_sparsify_model = False
self._experimental_disable_per_channel = False
self._debug_info = None  # contains the stack traces of all the original
# nodes in the `GraphDef` to the converter.
self.saved_model_dir = None
self._saved_model_tags = None
self._saved_model_version = 0
self._saved_model_exported_names = []
self._tflite_metrics = metrics.TFLiteConverterMetrics()
self._collected_converter_params = {}
self._experimental_disable_batchmatmul_unfold = False
self._experimental_lower_tensor_list_ops = True
self._experimental_default_to_single_batch_in_tensor_list_ops = False
self._experimental_unfold_large_splat_constant = False
self._experimental_tf_quantization_mode = None
# If unset, bias:int32 is by default except 16x8 quant.
# For 16x8 quant, bias:int64 is used to prevent any overflow by default.
self._experimental_full_integer_quantization_bias_type = None
# Initializes conversion metadata.
self.exclude_conversion_metadata = False
self._metadata = conversion_metdata_fb.ConversionMetadataT()
self._metadata.environment = conversion_metdata_fb.EnvironmentT()
self._metadata.options = conversion_metdata_fb.ConversionOptionsT()
self._metadata.environment.tensorflowVersion = versions.__version__
self._metadata.environment.modelType = self._get_original_model_type()
self._experimental_enable_dynamic_update_slice = False
self._experimental_preserve_assert_op = False
self._experimental_guarantee_all_funcs_one_use = False

# When the value is true, the MLIR quantantizer triggers dynamic range
# quantization in MLIR instead of the old quantizer. Used only if
# experimental_new_quantizer is on.
self.experimental_new_dynamic_range_quantizer = True
# Experimental flag to enable low-bit QAT in 8 bit.
self._experimental_low_bit_qat = False
# Experimental flag to add all TF ops (including custom TF ops) to the
# converted model as flex ops.
self._experimental_allow_all_select_tf_ops = False

self._experimental_variable_quantization = False
