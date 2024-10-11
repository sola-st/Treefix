# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if name == "post_training_quantize":
    warnings.warn("Property %s is deprecated, "
                  "please use optimizations=[Optimize.DEFAULT]"
                  " instead." % name)
    if value:
        self.optimizations = [Optimize.DEFAULT]
    else:
        self.optimizations = []
    exit()
if name == "target_ops":
    warnings.warn("Property %s is deprecated, please use "
                  "target_spec.supported_ops instead." % name)
    self.target_spec.supported_ops = value
    exit()
object.__setattr__(self, name, value)
