# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/c_api_util.py
super(ScopedTFGraph, self).__init__(
    name, obj=c_api.TF_NewGraph(), deleter=c_api.TF_DeleteGraph)
