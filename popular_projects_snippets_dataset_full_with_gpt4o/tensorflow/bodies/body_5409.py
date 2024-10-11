# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
if "colocate_with" in kwargs:
    with ops.device(None):
        with ops.colocate_with(kwargs["colocate_with"]):
            exit(next_creator(**kwargs))

self.assertIn("ps1", kwargs["name"])
with ops.device("/job:ps/task:1"):
    exit(next_creator(**kwargs))
