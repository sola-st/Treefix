# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/nadam.py
var_dtype = var_list[0].dtype.base_dtype
if self._m_cache is None:
    self._m_cache = self.add_weight(
        'momentum_cache',
        shape=[],
        dtype=var_dtype,
        initializer='ones',
        trainable=False,
        aggregation=tf_variables.VariableAggregation.ONLY_FIRST_REPLICA)
    self._weights.append(self._m_cache)
# Separate for-loops to respect the ordering of slot variables from v1.
for var in var_list:
    # Create slots for the first moments.
    self.add_slot(var, 'm')
for var in var_list:
    # Create slots for the second moments.
    self.add_slot(var, 'v')
