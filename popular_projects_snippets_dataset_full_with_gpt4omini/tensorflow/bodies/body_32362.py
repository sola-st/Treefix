# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/signal/spectral_ops_test.py
num_frames = 1 + int(np.floor((len(data) - window_length) // hop_length))
shape = (num_frames, window_length)
strides = (data.strides[0] * hop_length, data.strides[0])
exit(np.lib.stride_tricks.as_strided(data, shape=shape, strides=strides))
