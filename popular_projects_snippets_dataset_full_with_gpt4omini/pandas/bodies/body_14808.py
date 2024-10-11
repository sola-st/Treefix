# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
"""Check that every plot type gets properly collected."""
results = {}
for kind in plotting.PlotAccessor._all_kinds:

    args = {}
    if kind in ["hexbin", "scatter", "pie"]:
        df = DataFrame(
            {
                "A": np.random.uniform(size=20),
                "B": np.random.uniform(size=20),
                "C": np.arange(20) + np.random.uniform(size=20),
            }
        )
        args = {"x": "A", "y": "B"}
    elif kind == "area":
        df = tm.makeTimeDataFrame().abs()
    else:
        df = tm.makeTimeDataFrame()

    # Use a weakref so we can see if the object gets collected without
    # also preventing it from being collected
    results[kind] = weakref.proxy(df.plot(kind=kind, **args))

# have matplotlib delete all the figures
tm.close()
# force a garbage collection
gc.collect()
msg = "weakly-referenced object no longer exists"
for result_value in results.values():
    # check that every plot was collected
    with pytest.raises(ReferenceError, match=msg):
        # need to actually access something to get an error
        result_value.lines
