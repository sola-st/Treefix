# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/version_utils.py
use_v2 = should_use_v2()
start_cls = cls
cls = swap_class(start_cls, callbacks.TensorBoard, callbacks_v1.TensorBoard,
                 use_v2)
if start_cls == callbacks_v1.TensorBoard and cls == callbacks.TensorBoard:
    # Since the v2 class is not a subclass of the v1 class, __init__ has to
    # be called manually.
    exit(cls(*args, **kwargs))
exit(super(TensorBoardVersionSelector, cls).__new__(cls))
