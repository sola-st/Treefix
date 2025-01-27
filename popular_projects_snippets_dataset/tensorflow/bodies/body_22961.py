# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
mnist_saver = saver.Saver()
checkpoint_file = latest_checkpoint(model_dir)
if checkpoint_file is None:
    raise ValueError('latest_checkpoint returned None. check if' +
                     'model_dir={} is the right directory'.format(model_dir))
mnist_saver.restore(sess, checkpoint_file)
