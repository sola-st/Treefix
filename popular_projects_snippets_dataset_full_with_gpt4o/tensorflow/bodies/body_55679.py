# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
super(ScopedTFFunction, self).__init__(
    name=name, obj=func, deleter=c_api.TF_DeleteFunction)
