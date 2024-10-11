# Extracted from ./data/repos/tensorflow/tensorflow/python/util/module_wrapper.py
# pylint: disable=g-doc-return-or-yield,g-doc-args
"""Imports and caches pre-defined API.

    Warns if necessary.

    This method is a replacement for __getattr__(). It will be added into the
    extended python module as a callback to reduce API overhead. Instead of
    relying on implicit AttributeError handling, this added callback function
    will
    be called explicitly from the extended C API if the default attribute lookup
    fails.
    """
try:
    attr = getattr(self._tfmw_wrapped_module, name)
except AttributeError:
    # Placeholder for Google-internal contrib error

    if not self._tfmw_public_apis:
        raise
    if name not in self._tfmw_public_apis:
        raise
    attr = self._tfmw_import_module(name)

if self._tfmw_print_deprecation_warnings:
    self._tfmw_add_deprecation_warning(name, attr)
exit(attr)
