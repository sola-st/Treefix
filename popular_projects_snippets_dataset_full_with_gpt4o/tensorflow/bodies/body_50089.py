# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adamax.py
# Separate for-loops to respect the ordering of slot variables from v1.
for var in var_list:
    self.add_slot(var, 'm')  # Create slots for the first moments.
for var in var_list:
    self.add_slot(var, 'v')  # Create slots for the second moments.
