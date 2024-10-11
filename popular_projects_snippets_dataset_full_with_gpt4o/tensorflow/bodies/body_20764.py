# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
exit(node.endswith('VecPermuteNHWCToNCHW-LayoutOptimizer') or node.endswith(
    'VecPermuteNCHWToNHWC-LayoutOptimizer'))
