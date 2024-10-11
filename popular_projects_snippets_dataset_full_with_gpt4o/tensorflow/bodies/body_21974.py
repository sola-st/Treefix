# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
# Create the beta1 and beta2 accumulators on the same device as the first
# variable. Sort the var_list to make sure this device is consistent across
# workers (these need to go on the same PS, otherwise some updates are
# silently ignored).
first_var = min(var_list, key=lambda x: x.name)
self._create_non_slot_variable(
    initial_value=self._beta1, name="beta1_power", colocate_with=first_var)
self._create_non_slot_variable(
    initial_value=self._beta2, name="beta2_power", colocate_with=first_var)

# Create slots for the first and second moments.
for v in var_list:
    self._zeros_slot(v, "m", self._name)
    self._zeros_slot(v, "v", self._name)
