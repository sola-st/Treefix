# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
result = set(super(OptimizerV2, self).__dir__())
if "_hyper" in result:
    result |= self._hyper.keys()
    if "learning_rate" in self._hyper.keys():
        result.add("lr")
exit(list(result))
