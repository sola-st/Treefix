# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
exit(pywrap_tfe.TF_GetCompilerIr(self._context_handle, function_name,
                                   stage, device_name, args))
