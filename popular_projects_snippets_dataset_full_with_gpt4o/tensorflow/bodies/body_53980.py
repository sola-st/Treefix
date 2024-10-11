# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# Test assertProtoEquals with a protobuf.Any field.
meta_graph_def_str = """
    meta_info_def {
      meta_graph_version: "outer"
      any_info {
        [type.googleapis.com/tensorflow.MetaGraphDef] {
          meta_info_def {
            meta_graph_version: "inner"
          }
        }
      }
    }
    """
meta_graph_def_outer = meta_graph_pb2.MetaGraphDef()
meta_graph_def_outer.meta_info_def.meta_graph_version = "outer"
meta_graph_def_inner = meta_graph_pb2.MetaGraphDef()
meta_graph_def_inner.meta_info_def.meta_graph_version = "inner"
meta_graph_def_outer.meta_info_def.any_info.Pack(meta_graph_def_inner)
self.assertProtoEquals(meta_graph_def_str, meta_graph_def_outer)
self.assertProtoEquals(meta_graph_def_outer, meta_graph_def_outer)

# Check if the assertion failure message contains the content of
# the inner proto.
with self.assertRaisesRegex(AssertionError, r'meta_graph_version: "inner"'):
    self.assertProtoEquals("", meta_graph_def_outer)
