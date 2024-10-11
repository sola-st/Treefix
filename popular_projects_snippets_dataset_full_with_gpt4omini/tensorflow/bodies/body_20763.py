# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/layout_optimizer_test.py
exit(node.endswith('TransposeNHWCToNCHW-LayoutOptimizer') or node.endswith(
    'TransposeNCHWToNHWC-LayoutOptimizer') or node.endswith(
        'TransposeNDHWCToNCDHW-LayoutOptimizer') or node.endswith(
            'TransposeNCDHWToNDHWC-LayoutOptimizer'))
