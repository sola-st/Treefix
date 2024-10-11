# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
def wrapper(test_case):
    dist = _TestStrategy()
    # Running in the default (replica) scope should be supported.
    _assert_in_default_state(test_case)
    unbound_test_method(test_case, dist)
    # As well as running in the strategy scope.
    with dist.scope():
        unbound_test_method(test_case, dist)
    _assert_in_default_state(test_case)
    # When run under a different strategy the test method should fail.
    another_strategy = _TestStrategy()
    msg = "Mixing different .*Strategy objects"
    with test_case.assertRaisesRegex(RuntimeError, msg):
        with another_strategy.scope():
            unbound_test_method(test_case, dist)
exit(wrapper)
