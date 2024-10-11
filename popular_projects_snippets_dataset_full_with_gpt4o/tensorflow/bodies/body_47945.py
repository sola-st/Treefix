# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
if not self.trainable and self.built:
    exit([self.kernel, self.recurrent_kernel, self.bias])
exit([])
