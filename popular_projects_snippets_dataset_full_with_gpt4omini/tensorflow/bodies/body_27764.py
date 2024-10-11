# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py
exit(dataset_ops.Dataset.zip((x.batch(batch_size=size),
                                y.batch(batch_size=size),
                                z.batch(batch_size=size))))
