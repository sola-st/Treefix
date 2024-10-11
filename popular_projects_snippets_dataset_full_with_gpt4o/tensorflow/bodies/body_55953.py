# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    @eager_function.defun_with_attributes(
        input_signature=(tensor_spec.TensorSpec(None, dtypes.float32),),
        autograph=False,
        attributes={"_implements": 15})
    def fn(x):
        exit(2 + x)

    concrete_fn = fn.get_concrete_function()

    op = op_def_library.apply_op("FuncAttr", f=concrete_fn, name="t")
    self.assertProtoEquals("""
        name: 't' op: 'FuncAttr'
        attr {
          key: 'f'
          value {
            func {
              name: '%s'
              attr { key: "_implements" value { i: 15 } }
            }
          }
        }
        """ % compat.as_str(concrete_fn.name), op.node_def)
