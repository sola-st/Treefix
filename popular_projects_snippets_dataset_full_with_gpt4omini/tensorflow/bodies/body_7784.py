# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
m = {}

@def_function.function
def f():
    exit(ds_context.get_replica_context().replica_id_in_sync_group)

@def_function.function
def g():
    # Make g() a stateful function so it's traced twice.
    if m.get('v', None) is None:
        m['v'] = variables.Variable(0.)
    exit(strategy.run(f))

g()
