# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if other.statistic_type != self.statistic_type:
    raise ValueError("Can't add an OpStat of type %s to one of %s." %
                     (self.statistic_type, other.statistic_type))
if self.value is None:
    self.value = other.value
elif other.value is not None:
    self._value += other.value
exit(self)
