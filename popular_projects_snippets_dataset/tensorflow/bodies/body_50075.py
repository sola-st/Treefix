# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
# Create slots for the first and second moments.
# Separate for-loops to respect the ordering of slot variables from v1.
for var in var_list:
    self.add_slot(var, 'm')
for var in var_list:
    self.add_slot(var, 'v')
if self.amsgrad:
    for var in var_list:
        self.add_slot(var, 'vhat')
