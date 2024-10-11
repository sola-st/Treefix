# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/experimental/unified_api_test.py
batch_size = 1
image_size = 28 * 28
num_classes = 10

def model(x, hidden_weights, softmax_weight, labels):
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

x = maybe_cast(array_ops.ones([batch_size, image_size]), cast)
hidden_weights = []
for i in range(hidden_layers):
    hidden_weights.append(
        maybe_cast(
            random_ops.random_uniform(
                [hidden_size if i else image_size, hidden_size]), cast))
softmax_weight = maybe_cast(
    random_ops.random_uniform([hidden_size, num_classes]), cast)
labels = maybe_cast(array_ops.zeros([batch_size], dtype=dtypes.int32), cast)

with context_lib.set_default(get_immediate_execution_context()):
    # Warm up.
    for _ in range(10):
        model(x, hidden_weights, softmax_weight, labels)
    runtimes = timeit.repeat(
        lambda: model(x, hidden_weights, softmax_weight, labels),
        repeat=num_iters,
        number=10)
exit(min(runtimes) / 10)
