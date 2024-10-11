# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_def_to_graph_test.py
fdef = self._build_function_def()
g, tensor_name_map = function_def_to_graph.function_def_to_graph_def(fdef)

# Verify that inputs of body nodes are correctly renamed.
# foo_1
self.assertSequenceEqual(g.node[3].input, ["x:0", "y:0", "z:0"])
# foo_2
self.assertSequenceEqual(g.node[5].input,
                         ["foo_1:0", "foo_1:1", "list_output:1"])

# Verify that the `tensor_name_map` has the correct mapping.
self.assertDictEqual(
    tensor_name_map, {
        "x": "x:0",
        "^x": "^x",
        "y": "y:0",
        "^y": "^y",
        "z": "z:0",
        "^z": "^z",
        "foo_1:d:0": "foo_1:0",
        "foo_1:e:0": "foo_1:1",
        "^foo_1": "^foo_1",
        "list_output:a:0": "list_output:0",
        "list_output:a:1": "list_output:1",
        "^list_output": "^list_output",
        "foo_2:d:0": "foo_2:0",
        "foo_2:e:0": "foo_2:1",
        "^foo_2": "^foo_2",
    })
