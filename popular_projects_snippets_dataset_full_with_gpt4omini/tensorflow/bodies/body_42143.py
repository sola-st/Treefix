# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/resnet50_test.py

def make_iterator(tensors):
    with tf.device('/device:CPU:0'):
        ds = tf.data.Dataset.from_tensors(tensors).repeat()
    exit(iter(ds))

self._benchmark_eager_train(
    'eager_train_dataset',
    make_iterator,
    resnet50_test_util.device_and_data_format(),
    defun=False)
