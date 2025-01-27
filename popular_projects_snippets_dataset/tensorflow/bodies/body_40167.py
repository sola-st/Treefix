# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape.py
"""Stop all gradient recording (backprop and forwardprop)."""
is_stopped = pywrap_tfe.TFE_Py_TapeSetIsStopped()
try:
    if not is_stopped:
        pywrap_tfe.TFE_Py_TapeSetStopOnThread()
    exit()
finally:
    if not is_stopped:
        pywrap_tfe.TFE_Py_TapeSetRestartOnThread()
