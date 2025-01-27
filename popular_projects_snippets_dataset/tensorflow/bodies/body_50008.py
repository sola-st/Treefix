# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if "learning_rate" in self._hyper:
    lr_t = array_ops.identity(self._decayed_lr(var_dtype))
    apply_state[(var_device, var_dtype)]["lr_t"] = lr_t
