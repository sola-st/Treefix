# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adadelta.py
# Separate for-loops to respect the ordering of slot variables from v1.
for v in var_list:
    self.add_slot(v, 'accum_grad')
for v in var_list:
    self.add_slot(v, 'accum_var')
