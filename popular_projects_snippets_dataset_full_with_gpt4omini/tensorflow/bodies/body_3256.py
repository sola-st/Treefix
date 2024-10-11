# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/pywrap_quantize_model_test.py
saved_model_path = self.create_tempdir('saved_model').full_path
signature_def_keys = ['serving_default']
tags = {'serve'}
quant_opts_serialized = 'invalid protobuf serialization string'

with self.assertRaisesRegex(TypeError, 'incompatible function arguments'):
    pywrap_quantize_model.quantize_ptq_model_pre_calibration(
        saved_model_path, signature_def_keys, tags, quant_opts_serialized
    )
