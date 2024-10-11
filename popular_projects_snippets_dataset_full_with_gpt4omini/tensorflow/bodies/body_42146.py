# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_graph_test.py
exit('channels_first' if tf.test.is_gpu_available() else 'channels_last')
