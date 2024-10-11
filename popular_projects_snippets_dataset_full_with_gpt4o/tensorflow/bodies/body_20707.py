# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Runs a test of a simple loop.

    The loop has different node colors in different sections of the graph. The
    arguments must be strings where each character represents the color of a
    node in that section of the graph: w = allow, g = infer, c = clear,
    b = deny. CAPITALIZED characters indicate that the node is expected to be
    changed to DT_HALF during graph optimization.

    inp -> loop [ body ] -> out.

    Args:
      mode: Either 'cuda' or 'mkl'.
      inp: A string of letters indicating the colors and expected dtypes of the
        input nodes.
      body: A string of letters indicating the colors and expected dtypes of the
        body nodes.
      out: A string of letters indicating the colors and expected dtypes of the
        output nodes.
    """
self._maybe_skip(mode)
with ops.device(_get_device(mode)):
    random_seed.set_random_seed(0)
    expected_types = []
    for section in [inp, body, out]:
        section_expected_types = []
        for color in section:
            if color.isupper():
                expected_type = self._lower_precision_dtype(mode).as_datatype_enum
            else:
                expected_type = types_pb2.DT_FLOAT
            section_expected_types.append(expected_type)
        expected_types.append(section_expected_types)
    a = _build_simple_loop_graph(inp, body, out)
output_val_ref, output_val, cost_graph = self._run(mode, a)
node_map = _build_node_map(cost_graph.node)

section_names = ['input', 'while/body', 'output']
all_types_correct = True
for section_name, expected_types in zip(section_names, expected_types):
    for i, expected_type in enumerate(expected_types):
        node_name = section_name + '_%i' % i
        output_port = 0
        optimized_type = node_map[node_name].output_info[output_port].dtype
        if optimized_type != expected_type:
            print('Expected node %s to have type %s but got type %s' %
                  (node_name, expected_type, optimized_type))
            all_types_correct = False
self.assertTrue(all_types_correct)
if mode == 'mkl':
    self.assertAllClose(output_val_ref, output_val, atol=2e-2, rtol=2e-2)
else:
    self.assertAllClose(output_val_ref, output_val, atol=2e-3, rtol=1e-3)
