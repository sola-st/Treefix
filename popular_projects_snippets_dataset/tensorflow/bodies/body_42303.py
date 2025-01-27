# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Clears and re-initializes the TF JIT compiler flags.

  Should only be used for testing.
  """
pywrap_tfe.TF_ResetJitCompilerFlags()
