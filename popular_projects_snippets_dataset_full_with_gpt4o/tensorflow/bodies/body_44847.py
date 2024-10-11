# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
if self.options.user_requested:
    self.autograph_ctx.__enter__()
if self.use_name_scope:
    self.name_scope.__enter__()
if self.use_auto_deps:
    self.autodeps_scope.__enter__()
exit(self)
