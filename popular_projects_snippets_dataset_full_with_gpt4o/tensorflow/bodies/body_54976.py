# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py
api_def_map = c_api_util.ApiDefMap()
op_def = api_def_map.get_op_def("Add")
self.assertEqual(op_def.name, "Add")
api_def = api_def_map.get_api_def("Add")
self.assertEqual(api_def.graph_op_name, "Add")
