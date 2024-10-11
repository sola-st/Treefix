# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
if context.executing_eagerly():
    exit(self.read_value().numpy())
else:
    raise NotImplementedError("DistributedVariable.numpy() is only available "
                              "when eager execution is enabled.")
