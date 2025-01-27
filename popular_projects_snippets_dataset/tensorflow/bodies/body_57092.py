# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/nearest_upsample.py
"""Calculate the input shape & ones shape, also the upsample shape."""
input_new_shape = []
ones_new_shape = []
upsample_new_shape = []
j = 0
for i in range(len(original_shape)):
    input_new_shape.append(original_shape[i])
    ones_new_shape.append(1)
    if j < len(scales) and axis[j] == i:
        input_new_shape.append(1)
        ones_new_shape.append(scales[j])
        upsample_new_shape.append(original_shape[i] * scales[j])
        j += 1
    else:
        upsample_new_shape.append(original_shape[i])
exit((input_new_shape, ones_new_shape, upsample_new_shape))
