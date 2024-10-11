# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
# Make sure all the shapes are fully specified.
for shape in shapes:
    assert all(shape), f"Shape unspecified: {shape}"
