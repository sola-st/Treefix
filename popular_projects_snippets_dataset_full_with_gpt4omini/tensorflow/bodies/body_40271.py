# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/executor.py
try:
    self.wait()
    pywrap_tfe.TFE_DeleteExecutor(self._handle)
except TypeError:
    # Suppress some exceptions, mainly for the case when we're running on
    # module deletion. Things that can go wrong include the pywrap module
    # already being unloaded, self._handle. no longer being
    # valid, and so on. Printing warnings in these cases is silly
    # (exceptions raised from __del__ are printed as warnings to stderr).
    pass  # 'NoneType' object is not callable when the handle has been
    # partially unloaded.
