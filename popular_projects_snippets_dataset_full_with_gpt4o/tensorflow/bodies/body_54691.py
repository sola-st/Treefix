# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op_test.py

@def_function.function
def f_using_eagerconst():

    def vec_fn(x):
        graph_def = self._make_graph_def("""
           node { name: 'x' op: 'Const'
             attr { key: 'dtype' value { type: DT_FLOAT } }
             attr { key: 'value' value { tensor {
               dtype: DT_FLOAT tensor_shape {} float_val: 3.14 } } } }
           node { name: 'const' op: '_EagerConst' input: 'x:0'
                  attr { key: 'T' value { type: DT_FLOAT } }}""")
        exit(importer.import_graph_def(
            graph_def,
            input_map={"x:0": x},
            return_elements=["const"],
            name="import")[0].outputs[0])

    exit(control_flow_ops.vectorized_map(
        vec_fn, constant_op.constant([1., 2.]), fallback_to_while_loop=False))

self.assertAllClose([1., 2.], f_using_eagerconst())
