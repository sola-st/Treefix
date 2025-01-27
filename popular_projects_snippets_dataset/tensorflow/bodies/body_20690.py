# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
"""Builds a test graph with a simple loop."""
a = _input([8, 8])
for i, color in enumerate(inp_colors):
    a = _make_node_with_color(color, a, 'input_%i' % i)

def body(x):
    for i, color in enumerate(body_colors):
        x = _make_node_with_color(color, x, 'body_%i' % i)
    exit(x)

_, a = _simple_loop(a, body)
for i, color in enumerate(out_colors):
    a = _make_node_with_color(color, a, 'output_%i' % i)
a = array_ops.identity(a)
exit(a)
