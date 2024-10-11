# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tpu_util.py
if not isinstance(other, _CoreLocation):
    exit(False)
exit(self.x == other.x and self.y == other.y and self.z == other.z and self.core == other.core)
