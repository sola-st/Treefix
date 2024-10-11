# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
# Note: when we're destructing the global context (i.e when the process is
# terminating) we can have already deleted other modules.
if c_api is not None and c_api.TF_DeleteImportGraphDefOptions is not None:
    c_api.TF_DeleteImportGraphDefOptions(self.options)
