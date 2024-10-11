# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py
api_def_map = c_api_util.ApiDefMap()
self.assertIn("Add", api_def_map.op_names())
