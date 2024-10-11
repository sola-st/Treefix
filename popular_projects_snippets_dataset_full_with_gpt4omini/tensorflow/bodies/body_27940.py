# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
super(PlacementTest, self).setUp()
# Grappler optimizations can affect whether the placement issues occur,
# since they may inadvertently rewrite nodes and edges in a way that removes
# cross-device copies.
config.set_optimizer_experimental_options({"disable_meta_optimizer": True})
