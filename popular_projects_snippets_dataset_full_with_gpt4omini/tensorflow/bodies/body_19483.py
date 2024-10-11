# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
exit(gen_math_ops.maximum(
    ending_lr,
    starting_lr + ((ending_lr - starting_lr) * step_counter) /
    num_steps_float))
