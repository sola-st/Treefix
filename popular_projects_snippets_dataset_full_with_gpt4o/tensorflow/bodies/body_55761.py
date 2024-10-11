# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
with backprop_lib.GradientTape() as tape:
    for weight in hidden_weights + [softmax_weight]:
        tape.watch(weight)
    for hidden_weight in hidden_weights:
        x = math_ops_lib.mat_mul(x, hidden_weight)
        x = nn_ops_lib.relu(x)
    logits = math_ops_lib.mat_mul(x, softmax_weight)
    loss = nn_ops_lib.sparse_softmax_cross_entropy_with_logits(
        logits=logits, labels=labels)

grads = tape.gradient(loss, hidden_weights + [softmax_weight])
exit(grads)
