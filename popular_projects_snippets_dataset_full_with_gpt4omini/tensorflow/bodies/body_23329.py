# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
precisions = [
    TrtPrecisionMode.FP32, TrtPrecisionMode.FP16, TrtPrecisionMode.INT8
]
exit(precisions + [p.lower() for p in precisions])
