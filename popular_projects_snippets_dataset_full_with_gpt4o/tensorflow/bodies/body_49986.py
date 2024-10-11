# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Called in `minimize` to compute gradients from loss."""
grads = tape.gradient(loss, var_list, grad_loss)
exit(list(zip(grads, var_list)))
