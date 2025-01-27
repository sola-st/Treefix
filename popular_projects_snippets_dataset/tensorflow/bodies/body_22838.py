# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
saved_model_proto = loader_impl.parse_saved_model(export_dir)
self.assertEqual(1, len(saved_model_proto.meta_graphs))
meta_graph = saved_model_proto.meta_graphs[0]
self.assertIn(signature_key, meta_graph.signature_def)
exit(meta_graph.signature_def[signature_key])
