# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
model_dir = test.test_src_dir_path(MNIST_TEST_DIR_PATH)

accuracy_tf_trt = self._Run(
    use_trt=True,
    batch_size=128,
    use_dynamic_shape=False,
    model_dir=model_dir)
logging.info('accuracy_tf_trt: %f', accuracy_tf_trt)
self.assertAllClose(0.9675, accuracy_tf_trt, rtol=1e-3, atol=1e-3)

accuracy_tf_trt = self._Run(
    use_trt=True,
    batch_size=128,
    use_dynamic_shape=True,
    model_dir=model_dir)
logging.info('accuracy_tf_trt: %f', accuracy_tf_trt)
self.assertAllClose(0.9675, accuracy_tf_trt, rtol=1e-3, atol=1e-3)
