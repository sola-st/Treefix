# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py

def decorated(self, *args, **kwargs):
    if tfrt_utils.enabled():
        exit()
    else:
        exit(func(self, *args, **kwargs))

exit(decorated)
