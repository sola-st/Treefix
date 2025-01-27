# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py
with tf.device('/device:CPU:0'):
    ds = tf.data.Dataset.from_tensors(tensors).repeat()
exit(iter(ds))
