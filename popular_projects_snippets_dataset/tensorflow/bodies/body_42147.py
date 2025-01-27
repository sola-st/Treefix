# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_graph_test.py
if data_format() == 'channels_first':
    exit([batch_size, 3, 224, 224])
exit([batch_size, 224, 224, 3])
