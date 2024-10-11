# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
self.ones_rank_cache().flush()
self.zeros_cache().flush()
pywrap_tfe.TFE_ClearScalarCache()
