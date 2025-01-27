# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
# multiple yields: all arrays
for shape in [(1, 128), (16, 128), (256, 128)]:
    exit(np.random.random_sample(shape).astype(np.float32))
