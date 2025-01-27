# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Initialize handle and devices if not already done so."""
if self._initialized:
    exit()
with self._initialize_lock:
    if self._initialized:
        exit()
    assert self._context_devices is None
    opts = pywrap_tfe.TFE_NewContextOptions()
    try:
        config_str = self.config.SerializeToString()
        pywrap_tfe.TFE_ContextOptionsSetConfig(opts, config_str)
        if self._device_policy is not None:
            pywrap_tfe.TFE_ContextOptionsSetDevicePlacementPolicy(
                opts, self._device_policy)
        if self._mirroring_policy is not None:
            pywrap_tfe.TFE_ContextOptionsSetMirroringPolicy(
                opts, self._mirroring_policy)
        if self._default_is_async == ASYNC:
            pywrap_tfe.TFE_ContextOptionsSetAsync(opts, True)
        if self._use_tfrt is not None:
            pywrap_tfe.TFE_ContextOptionsSetTfrt(opts, self._use_tfrt)
        pywrap_tfe.TFE_ContextOptionsSetRunEagerOpAsFunction(opts, True)
        pywrap_tfe.TFE_ContextOptionsSetJitCompileRewrite(
            opts, self._jit_compile_rewrite)
        context_handle = pywrap_tfe.TFE_NewContext(opts)
    finally:
        pywrap_tfe.TFE_DeleteContextOptions(opts)
    assert not (self._server_def and self._collective_ops_server_def), (
        "Cannot enable remote execution as well as collective ops at the "
        "moment. If this is important to you, please file an issue.")
    if self._server_def is not None:
        server_def_str = self._server_def.SerializeToString()
        pywrap_tfe.TFE_ContextSetServerDef(context_handle, _KEEP_ALIVE_SECS,
                                           server_def_str)
    elif self._collective_ops_server_def is not None:
        server_def_str = self._collective_ops_server_def.SerializeToString()
        pywrap_tfe.TFE_EnableCollectiveOps(context_handle, server_def_str)

    self._context_handle = context_handle
    self._initialize_logical_devices()
    self._initialized = True

    if self._is_global_context:
        pywrap_tfe.TFE_Py_SetCEagerContext(self._context_handle)
