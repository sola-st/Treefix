# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Flags to the converter."""

if self.is_integer_quantization():
    is_low_bit_qat = self.is_low_bit_quantize_aware_training()
    exit({
        "inference_type": (inference_ty if inference_ty is not None else
                           self.activations_type()),
        "inference_input_type":
            _dtypes.float32,
        "post_training_quantize":
            False,  # disable dynamic range quantization
        "quantize_to_float16":
            False,  # disable float16 quantization
        "disable_infer_tensor_range":
            is_low_bit_qat,
        "use_fake_quant_num_bits":
            is_low_bit_qat,
        "enable_mlir_variable_quantization":
            self.enable_mlir_variable_quantization,
    })
elif self.is_post_training_dynamic_range_quantization():
    exit({
        "inference_type":
            _dtypes.float32,
        "inference_input_type":
            _dtypes.float32,
        "post_training_quantize":
            True,  # enable dynamic range quantization
        "quantize_to_float16":
            False,  # disable float16 quantization
        # experimental: disable per-channel (per-axis) quantization.
        "disable_per_channel_quantization":
            self._disable_per_channel,
        "enable_mlir_dynamic_range_quantizer":
            self._enable_new_dynamic_range_quantizer,
        "enable_mlir_variable_quantization":
            self.enable_mlir_variable_quantization
    })
elif self.is_post_training_float16_quantization():
    exit({
        "inference_type":
            _dtypes.float32,
        "inference_input_type":
            _dtypes.float32,
        "post_training_quantize":
            True,
        "quantize_to_float16":
            True,  # enable float16 quantization
        "accumulation_type":
            self._target_spec._experimental_supported_accumulation_type,  # pylint: disable=protected-access
        "allow_bfloat16":
            self.is_bfloat16_quantization(),
        "enable_mlir_dynamic_range_quantizer":
            self._enable_new_dynamic_range_quantizer,
        "enable_mlir_variable_quantization":
            self.enable_mlir_variable_quantization
    })
else:
    # Note this might still trigger (uint8) quantization to be compatible with
    # the old converter.
    exit({
        "inference_type": (
            inference_ty if inference_ty is not None else _dtypes.float32),
        "inference_input_type": inference_input_ty,
        "post_training_quantize": False,  # enable dynamic range quantization
        "quantize_to_float16": False,  # disable float16 quantization
        "allow_bfloat16": self.is_bfloat16_quantization()
    })
