# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py

def step(features, weights):
    exit(mid_level_api(features, weights))

exit(strategy.run(step, args=(features, weights)))
