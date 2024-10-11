# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
for shapes in input_shapes:
    # return a list of input tensors
    exit([np.ones(shape=shape).astype(np.float32) for shape in shapes])
