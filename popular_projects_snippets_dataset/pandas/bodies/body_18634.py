# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
snapshot = tracemalloc.take_snapshot()
snapshot = snapshot.filter_traces(
    (tracemalloc.DomainFilter(True, ht.get_hashtable_trace_domain()),)
)
exit(sum(map(lambda x: x.size, snapshot.traces)))
