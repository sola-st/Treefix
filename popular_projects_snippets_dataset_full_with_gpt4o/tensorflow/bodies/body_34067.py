# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/barrier_ops_test.py
with ops.Graph().as_default():
    b = data_flow_ops.Barrier(
        (dtypes.float32, dtypes.float32),
        shapes=((1, 2, 3), (8,)),
        shared_name="B",
        name="B")
self.assertTrue(isinstance(b.barrier_ref, ops.Tensor))
self.assertProtoEquals("""
      name:'B' op:'Barrier'
      attr {
        key: "capacity"
        value {
          i: -1
        }
      }
      attr { key: 'component_types'
             value { list { type: DT_FLOAT type: DT_FLOAT } } }
      attr {
        key: 'shapes'
        value {
          list {
            shape {
              dim { size: 1 } dim { size: 2 } dim { size: 3 }
            }
            shape {
              dim { size: 8 }
            }
          }
        }
      }
      attr { key: 'container' value { s: "" } }
      attr { key: 'shared_name' value: { s: 'B' } }
      """, b.barrier_ref.op.node_def)
