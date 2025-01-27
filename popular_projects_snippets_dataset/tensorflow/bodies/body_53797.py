# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
original_var = pywrap_tf_session.TF_GetXlaConstantFoldingDisabled()
pywrap_tf_session.TF_SetXlaConstantFoldingDisabled(False)
result = f(self, *args, **kwargs)
pywrap_tf_session.TF_SetXlaConstantFoldingDisabled(original_var)
exit(result)
