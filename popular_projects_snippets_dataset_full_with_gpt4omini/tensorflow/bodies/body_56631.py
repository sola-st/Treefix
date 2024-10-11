# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
options = debugger.QuantizationDebugOptions(
    layer_debug_metrics={'l1_norm': lambda diffs: np.mean(np.abs(diffs))})
if not from_converter:
    if quantized_io:
        debug_model = QuantizationDebuggerTest.debug_model_int8
    else:
        debug_model = QuantizationDebuggerTest.debug_model_float
    quant_debugger = debugger.QuantizationDebugger(
        quant_debug_model_content=debug_model,
        debug_dataset=_calibration_gen,
        debug_options=options)
else:
    options.fully_quantize = quantized_io
    quant_debugger = debugger.QuantizationDebugger(
        converter=_quantize_converter(self.tf_model_root, self.tf_model,
                                      _calibration_gen),
        debug_dataset=_calibration_gen,
        debug_options=options)

quant_debugger.run()

expected_quant_io_metrics = {
    'num_elements': 9,
    'stddev': 0.03850026,
    'mean_error': 0.01673192,
    'max_abs_error': 0.10039272,
    'mean_squared_error': 0.0027558778,
    'l1_norm': 0.023704167,
}
expected_float_io_metrics = {
    'num_elements': 9,
    'stddev': 0.050998904,
    'mean_error': 0.007843441,
    'max_abs_error': 0.105881885,
    'mean_squared_error': 0.004357292,
    'l1_norm': 0.035729896,
}
expected_metrics = (
    expected_quant_io_metrics
    if quantized_io else expected_float_io_metrics)
self.assertLen(quant_debugger.layer_statistics, 1)
actual_metrics = next(iter(quant_debugger.layer_statistics.values()))

self.assertCountEqual(expected_metrics.keys(), actual_metrics.keys())
for key, value in expected_metrics.items():
    self.assertAlmostEqual(value, actual_metrics[key], places=5)

buffer = io.StringIO()
quant_debugger.layer_statistics_dump(buffer)
reader = csv.DictReader(buffer.getvalue().split())
actual_values = next(iter(reader))

expected_values = expected_metrics.copy()
expected_values.update({
    'op_name': 'CONV_2D',
    'tensor_idx': 7,
    'scale': 0.15686275,
    'zero_point': -128,
    'tensor_name': r'Identity[1-9]?$'
})
for key, value in expected_values.items():
    if isinstance(value, str):
        self.assertIsNotNone(
            re.match(value, actual_values[key]),
            'String is different from expected string. Please fix test code if'
            " it's being affected by graph manipulation changes.")
    elif isinstance(value, list):
        self.assertAlmostEqual(
            value[0], float(actual_values[key][1:-1]), places=5)
    else:
        self.assertAlmostEqual(value, float(actual_values[key]), places=5)
