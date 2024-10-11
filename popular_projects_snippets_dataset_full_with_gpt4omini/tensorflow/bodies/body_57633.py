# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_test.py
np.random.seed(0)
inp = array_ops.placeholder(
    dtype=dtypes.float32, shape=(1, 5, 5, 3), name='input')
conv = nn_ops.conv2d(
    inp,
    filter=array_ops.ones([3, 3, 3, num_filters]),
    strides=[1, 1, 1, 1],
    padding='SAME')
output = nn_ops.relu(conv, name='output')

def calibration_gen():
    for _ in range(5):
        exit([np.random.uniform(-1, 1, size=(1, 5, 5, 3)).astype(np.float32)])

exit((inp, output, calibration_gen))
