# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
producer_op_list = op_def_pb2.OpList()
text_format.Merge("""
      op {
        name: 'OpWithFutureDefaultAttr'
        attr { name: 'default_int' type: 'int' default_value { i: 456 } }
      }
    """, producer_op_list)
# Attr only in producer_op_list with default value gets removed.
with ops.Graph().as_default():
    a = importer.import_graph_def(
        self._MakeGraphDef("""
          node { name: 'A' op: 'OpWithFutureDefaultAttr'
                 attr { key: 'default_int' value { i: 456 } } }
          """),
        return_elements=["A"],
        producer_op_list=producer_op_list)
    with self.assertRaisesRegex(
        ValueError, "Operation 'import/A' has no attr named 'default_int'."):
        a[0].get_attr("default_int")
