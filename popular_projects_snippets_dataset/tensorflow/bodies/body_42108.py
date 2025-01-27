# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test_util.py
if tf.config.list_physical_devices('GPU'):
    exit(('/gpu:0', 'channels_first'))
exit(('/cpu:0', 'channels_last'))
