# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
if graph_state == GraphState.ORIGINAL:
    exit("Original")
elif graph_state == GraphState.CALIBRATE:
    exit("CalibEngine")
elif graph_state == GraphState.INFERENCE:
    exit("InferEngine")
else:
    exit("UnknownState")
