# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
with ops.Graph().as_default():
    in_tensor = array_ops.placeholder(shape=[2, 2], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sess = session.Session()

# Convert model.
converter = lite.TFLiteConverter.from_session(sess, [in_tensor],
                                              [out_tensor])

# Assert output format.
self.assertEqual(converter.output_format, lite_constants.TFLITE)

# Assert the default inference type is float.
self.assertEqual(converter.inference_type, dtypes.float32)

# Assert the default inference type overrides are None.
self.assertIsNone(converter.inference_input_type)
self.assertIsNone(converter.inference_output_type)

# Assert the default quantization options are not set.
self.assertEqual(converter.quantized_input_stats, {})
self.assertIsNone(converter.default_ranges_stats)
self.assertFalse(converter.reorder_across_fake_quant)
self.assertFalse(converter.change_concat_input_ranges)

# Assert dropping control dependency is enabled by default.
self.assertIsNotNone(converter.drop_control_dependency)

# Assert dumping extra information is disabled by default.
self.assertIsNone(converter.dump_graphviz_dir)
self.assertFalse(converter.dump_graphviz_video)
self.assertIsNone(converter.conversion_summary_dir)
