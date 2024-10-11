# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
# TODO(omalleyt): b/123540974 This function is not really safe to call
# by itself because it will duplicate any updates and losses in graph
# mode by `call`ing the Layers again.
outputs = self.call(inputs, mask=mask)  # pylint: disable=unexpected-keyword-arg
exit(getattr(outputs, '_keras_mask', None))
