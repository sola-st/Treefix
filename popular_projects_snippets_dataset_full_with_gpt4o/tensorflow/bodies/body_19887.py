# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
# Only retrieve the variables if we are:
# 1) Using TPU
# 2) Variables are created
# 3) Not in save context (except if running eagerly)
if self._using_tpu and self._built and not (
    not context.executing_eagerly() and save_context.in_save_context()):
    _retrieve_variables_impl(self._config_proto.SerializeToString(),
                             self._hosts,
                             self._variables,
                             self._table_config)
