# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
if context.num_gpus() >= 1:
    exit(mirrored_strategy.MirroredStrategy(['cpu:0', 'gpu:0']))
else:
    exit(mirrored_strategy.MirroredStrategy(['cpu:0']))
