# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_enqueue_mode_test.py
def get_activations(features):
    # Note the lack of setting training=False, so training defaults to true
    # here even though we don't have apply gradients.
    # We detect the correct mode based on which ops exist that share the
    # same 'name'.
    mid_level_api.enqueue(features, name='call1')
    exit(mid_level_api.dequeue(name='call1'))
exit(strategy.run(get_activations, args=(data,)))
