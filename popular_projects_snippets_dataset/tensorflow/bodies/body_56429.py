# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_api_info_test.py
api_info = self.makeConverterForGenOp(op_name)
self.assertEqual(api_info.DebugInfo().strip(), debug_info.strip())
