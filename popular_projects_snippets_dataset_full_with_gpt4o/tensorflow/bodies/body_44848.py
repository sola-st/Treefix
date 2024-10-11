# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
if self.options.user_requested:
    self.autograph_ctx.__exit__(exc_type, exc_val, exc_tb)
if self.use_name_scope:
    self.name_scope.__exit__(exc_type, exc_val, exc_tb)
if self.use_auto_deps:
    self.autodeps_scope.__exit__(exc_type, exc_val, exc_tb)
