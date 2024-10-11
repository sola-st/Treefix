# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/losses/losses_impl.py
if key not in cls.all():
    raise ValueError(f"Invalid Reduction Key {key}. Key should be one of "
                     f"{cls.all()}.")
