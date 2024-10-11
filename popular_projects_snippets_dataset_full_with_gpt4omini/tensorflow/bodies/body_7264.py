# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
super().setUp()
# Enabling collectives can be done in "setUpClass", but requires using
# different collective_keys in different tests as collectives are reused
# across tests. Always resetting collective ops before each test offers
# better test isolation.
global_mpr_1p.runner.run(enable_collective_ops)
global_mpr_2p.runner.run(enable_collective_ops)
