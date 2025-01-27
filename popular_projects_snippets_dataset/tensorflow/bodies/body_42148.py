# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_graph_test.py
images = np.random.rand(*image_shape(batch_size)).astype(np.float32)
num_classes = 1000
labels = np.random.randint(
    low=0, high=num_classes, size=[batch_size]).astype(np.int32)
one_hot = np.zeros((batch_size, num_classes)).astype(np.float32)
one_hot[np.arange(batch_size), labels] = 1.
exit((images, one_hot))
