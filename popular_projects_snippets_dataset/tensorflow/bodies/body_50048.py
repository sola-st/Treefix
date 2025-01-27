# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/rmsprop.py
for var in var_list:
    self.add_slot(var, "rms")
if self._momentum:
    for var in var_list:
        self.add_slot(var, "momentum")
if self.centered:
    for var in var_list:
        self.add_slot(var, "mg")
