# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Add a function definition to the context.

    Once added, the function (identified by its name) can be executed like any
    other operation.

    Args:
      fdef: A FunctionDef protocol buffer message.
    """
self.ensure_initialized()
fdef_string = fdef.SerializeToString()
pywrap_tfe.TFE_ContextAddFunctionDef(self._handle, fdef_string,
                                     len(fdef_string))
