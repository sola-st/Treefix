# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
if _is_running_on_cpu():
    exit(fc_lib.EmbeddingColumn.create_state(
        self, state_manager))

# Create state is called for the EmbeddingColumn to create its embedding
# variables under feature column V2, if we are on TPU so record the scope
# here.
_record_variable_scope_and_name(
    self.get_embedding_var_name(),
    'embedding_weights',
    bypass_scope_validation=self._bypass_scope_validation)
