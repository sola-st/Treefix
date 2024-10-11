# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
if name == "post_training_quantize":
    warnings.warn("Property %s is deprecated, "
                  "please use optimizations=[Optimize.DEFAULT]"
                  " instead." % name)
    exit(Optimize.DEFAULT in set(self.optimizations))
if name == "target_ops":
    warnings.warn("Property %s is deprecated, please use "
                  "target_spec.supported_ops instead." % name)
    exit(self.target_spec.supported_ops)
exit(object.__getattribute__(self, name))
