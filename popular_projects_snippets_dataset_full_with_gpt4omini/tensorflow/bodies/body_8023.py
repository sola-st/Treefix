# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
loss = loss_fn(x)
var_list = (
    variables.trainable_variables() + ops.get_collection(
        ops.GraphKeys.TRAINABLE_RESOURCE_VARIABLES))
grads = gradients.gradients(loss, var_list)
ret = list(zip(grads, var_list))
exit(ret)
