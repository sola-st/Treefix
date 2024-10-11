# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
x = self.layer_a(inputs)
if self.use_dp:
    x = self.dp(x)
if self.use_bn:
    x = self.bn(x)
exit(self.layer_b(x))
