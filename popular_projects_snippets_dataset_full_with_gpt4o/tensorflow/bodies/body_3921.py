# Extracted from ./data/repos/tensorflow/tensorflow/core/function/runtime_client/runtime_client_test.py
fndef = text_format.Parse(
    """
            signature {
               name: 'NullaryFunction'
               output_arg { name: 'o' type: DT_INT32 }
             }
             node_def {
               name: 'retval'
               op: 'Const'
               attr {
                 key: 'dtype'
                 value { type: DT_INT32 }
               }
               attr {
                 key: 'value'
                 value {
                   tensor {
                     dtype: DT_INT32
                     tensor_shape {}
                     int_val: 1
                   }
                 }
               }
             }
             ret { key: 'o' value: 'retval:output' }
         """,
    function_pb2.FunctionDef(),
)

ctx = runtime_client.GlobalEagerContext()
rt = runtime_client.Runtime(ctx)
rt.CreateFunction(fndef)
