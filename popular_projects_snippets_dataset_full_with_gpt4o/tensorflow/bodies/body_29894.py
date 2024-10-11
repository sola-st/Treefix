# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_test.py
# Load graph generated from earlier version of TF where
# placeholder shape was not set.
#
# a = tf.compat.v1.placeholder(tf.float32)
# b = a + 1.0
#
# Older graph's default shape is 'shape {}', not 'shape {
# unknown_rank: true }'
graph = """
node {
  name: "Placeholder"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "shape"
    value {
      shape {
      }
    }
  }
}
node {
  name: "add/y"
  op: "Const"
  attr {
    key: "dtype"
    value {
      type: DT_FLOAT
    }
  }
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
        }
        float_val: 1.0
      }
    }
  }
}
node {
  name: "add"
  op: "Add"
  input: "Placeholder"
  input: "add/y"
  attr {
    key: "T"
    value {
      type: DT_FLOAT
    }
  }
}
versions {
  producer: 21
}
"""
gdef = graph_pb2.GraphDef()
text_format.Merge(graph, gdef)
with self.cached_session():
    p, ret = importer.import_graph_def(
        gdef, return_elements=["Placeholder:0", "add:0"])

    # Feed in a vector of two elements.  Since the producer version
    # of 21, a shape of {} is interpreted as "any shape".  If
    # producer version were 22, then we'd get a shape mismatch
    # error.
    self.assertAllEqual([2.0, 3.0], ret.eval(feed_dict={p: [1.0, 2.0]}))
