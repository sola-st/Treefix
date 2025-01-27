# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Execute the test only if tfrt is not enabled."""

if tf_inspect.isclass(cls_or_func):
    if tfrt_utils.enabled():
        exit(None)
    else:
        exit(cls_or_func)
else:
    def decorator(func):

        def decorated(self, *args, **kwargs):
            if tfrt_utils.enabled():
                exit()
            else:
                exit(func(self, *args, **kwargs))

        exit(decorated)

    if cls_or_func is not None:
        exit(decorator(cls_or_func))

    exit(decorator)
