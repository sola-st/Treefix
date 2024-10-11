# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Clears and re-initializes the singleton context.

  Should only be used for testing.
  """
global _context
global _device_parsing_cache

# Garbage collect and clear scalar cache to avoid Tensor from current context
# polluting next context.
gc.collect()
pywrap_tfe.TFE_ClearScalarCache()
with _context_lock:
    if _context is not None:
        _context._clear_caches()
        _context = None
_create_context()
_device_parsing_cache = {}
