# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
if self._momentum:
    for var in var_list:
        self.add_slot(var, "momentum")
