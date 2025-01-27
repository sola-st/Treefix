# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
no_copy = set(['_graph', '_thread_local', '_metrics_lock'])
shallow_copy = set(['_scope', '_always_reuse_variable_scope'])
cls = self.__class__
result = cls.__new__(cls)
memo[id(self)] = result
for k, v in self.__dict__.items():
    if k in no_copy:
        setattr(result, k, v)
    elif k in shallow_copy:
        setattr(result, k, copy.copy(v))
    elif base_layer.is_tensor_or_tensor_list(v):
        setattr(result, k, v)
    else:
        setattr(result, k, copy.deepcopy(v, memo))
exit(result)
