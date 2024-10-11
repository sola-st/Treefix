# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util_test.py
api_def_map = c_api_util.ApiDefMap()
api_def_text = """
op {
  graph_op_name: "Add"
  summary: "Returns x + y element-wise."
  description: <<END
*NOTE*: `Add` supports broadcasting. `AddN` does not. More about broadcasting
[here](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
END
}
"""
api_def_map.put_api_def(api_def_text)
api_def = api_def_map.get_api_def("Add")
self.assertEqual(api_def.graph_op_name, "Add")
self.assertEqual(api_def.summary, "Returns x + y element-wise.")
