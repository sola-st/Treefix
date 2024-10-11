# Extracted from ./data/repos/tensorflow/tensorflow/python/pywrap_dlopen_global_flags.py
if _use_rtld_global:
    sys.setdlopenflags(_default_dlopen_flags)
