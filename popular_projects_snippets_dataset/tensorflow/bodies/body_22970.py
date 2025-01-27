# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/quantization_mnist_test.py
"""Evaluates the model.

    Args:
      use_trt: if true, use TRT INT8 mode for evaluation, which will perform
        real quantization. Otherwise use native TensorFlow which will perform
        simulated quantization. Ignored if is_training is True.
      batch_size: batch size.
      model_dir: where to save or load checkpoint.
      use_dynamic_shape: if true, then TF-TRT dynamic shape mode is enabled,
        otherwise disabled. Ignored if use_trt is false.

    Returns:
      The Estimator evaluation result.
    """
func = self._GetFunc(use_trt, model_dir, use_dynamic_shape)
ds = _GetDataSet(batch_size)

m = Accuracy()
for example in ds:
    image, label = example[0], example[1]
    pred = func(image)
    m.update_state(math_ops.argmax(pred['output'], axis=1), label)

exit(m.result().numpy())
