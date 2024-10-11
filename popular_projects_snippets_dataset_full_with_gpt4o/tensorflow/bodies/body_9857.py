# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli_test.py
ref_tensor_info = meta_graph_pb2.TensorInfo(
    dtype=types_pb2.DT_FLOAT_REF)
with captured_output() as (out, err):
    saved_model_cli._print_tensor_info(ref_tensor_info)
self.assertIn('DT_FLOAT_REF', out.getvalue().strip())
self.assertEqual(err.getvalue().strip(), '')
