# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/pywrap_quantize_model_test.py
saved_model_path = self.create_tempdir('saved_model').full_path
signature_def_keys = ['serving_default']
tags = {'serve'}
invalid_quant_opts_object = ('a', 'b', 'c')

with self.assertRaisesRegex(TypeError, 'incompatible function arguments'):
    pywrap_quantize_model.quantize_ptq_model_pre_calibration(
        saved_model_path, signature_def_keys, tags, invalid_quant_opts_object
    )
