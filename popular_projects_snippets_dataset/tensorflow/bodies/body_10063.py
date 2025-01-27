# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_lib.py
if node.op == "BatchNormWithGlobalNormalization":
    exit(node.attr["scale_after_normalization"].b)
exit(True)
