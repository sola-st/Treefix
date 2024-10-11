# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
exit((backend.is_tpu_strategy(strategy) and
        strategy.extended.num_hosts > 1))
