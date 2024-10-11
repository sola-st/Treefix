# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.Graph().as_default() as g:
    t1, t2, t3, t4, t5 = _apply_op(g, "FiveFloatOutputs", [],
                                   [dtypes.float32] * 5)
    t1.set_shape(None)
    t2.set_shape([])
    t3.set_shape([None])
    t4.set_shape([43, 37])
    t5.set_shape([43, None])

    b = constant_op.constant(1.0)  # pylint: disable=unused-variable

    gd = g.as_graph_def(add_shapes=True)
    self.assertProtoEqualsVersion("""
      node { name: "FiveFloatOutputs" op: "FiveFloatOutputs"
        attr {
          key: "_output_shapes"
          value {
            list {
              shape { unknown_rank: true }
              shape { }
              shape { dim { size: -1 } }
              shape { dim { size: 43 } dim { size: 37 } }
              shape { dim { size: 43 } dim { size: -1 } }
            }
          }
        }
      }
    node { name: "Const" op: "Const"
      attr {
        key: "_output_shapes"
        value {
          list {
            shape { }
          }
        }
      }
      attr {
        key: "dtype"
        value { type: DT_FLOAT }
      }
      attr {
        key: "value"
        value {
          tensor {
            dtype: DT_FLOAT
            tensor_shape { }
         float_val: 1.0  } } } }
      """, gd)
