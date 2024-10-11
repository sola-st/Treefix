# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
self.assertEqual(node_map[node_name].output_info[output_port].dtype,
                 self._lower_precision_dtype(mode).as_datatype_enum)
