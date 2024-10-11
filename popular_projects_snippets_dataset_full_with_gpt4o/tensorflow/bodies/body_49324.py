# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
if len(self.thresholds) == 1:
    result = self.accumulator[0]
else:
    result = self.accumulator
exit(ops.convert_to_tensor_v2_with_dispatch(result))
