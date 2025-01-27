# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
from l3.Runtime import _l_
"""Enables tracing of op execution via RunMetadata.

    To retrieve the accumulated metadata call context.export_run_metadata()
    and to stop tracing call context.disable_run_metadata().
    """
self.ensure_initialized()
_l_(20200)
pywrap_tfe.TFE_ContextEnableRunMetadata(self._handle)
_l_(20201)
