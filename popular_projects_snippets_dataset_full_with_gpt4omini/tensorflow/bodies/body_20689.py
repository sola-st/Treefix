# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/auto_mixed_precision_test.py
for i, color in enumerate(body_colors):
    x = _make_node_with_color(color, x, 'body_%i' % i)
exit(x)
