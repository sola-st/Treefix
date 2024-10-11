# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
spec = saveable_object.SaveSpec(
    tensor, "", name, dtype=dtype, device=device)
super(NoRestoreSaveable, self).__init__(tensor, [spec], name)
