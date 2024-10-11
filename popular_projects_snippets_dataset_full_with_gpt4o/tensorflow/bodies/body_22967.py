# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py

model_dir = test.test_src_dir_path(MNIST_TEST_DIR_PATH)

accuracy_tf_native = self._Run(
    is_training=False,
    use_trt=False,
    batch_size=128,
    num_epochs=None,
    model_dir=model_dir)['accuracy']
logging.info('accuracy_tf_native: %f', accuracy_tf_native)
self.assertAllClose(0.9662, accuracy_tf_native, rtol=3e-3, atol=3e-3)

accuracy_tf_trt = self._Run(
    is_training=False,
    use_trt=True,
    batch_size=128,
    num_epochs=None,
    model_dir=model_dir)['accuracy']
logging.info('accuracy_tf_trt: %f', accuracy_tf_trt)
self.assertAllClose(0.9675, accuracy_tf_trt, rtol=1e-3, atol=1e-3)
