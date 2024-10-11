# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op_test.py
graph_def = self._make_graph_def("""
         node { name: 'x' op: 'Const'
           attr { key: 'dtype' value { type: DT_FLOAT } }
           attr { key: 'value' value { tensor {
             dtype: DT_FLOAT tensor_shape {} float_val: NaN } } } }
         node { name: 'const' op: '_EagerConst' input: 'x:0'
                attr { key: 'T' value { type: DT_FLOAT } }}""")
x_id = importer.import_graph_def(
    graph_def,
    input_map={"x:0": x},
    return_elements=["const"],
    name="import")[0].outputs[0]
exit(x_id)
