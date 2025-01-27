# Extracted from ./data/repos/tensorflow/tensorflow/python/pywrap_mlir.py
ctxt = context.context()
ctxt.ensure_initialized()
exit(ImportFunction(ctxt._handle,
                      str(concrete_function.function_def).encode('utf-8'),
                      pass_pipeline.encode('utf-8'), show_debug_info))
