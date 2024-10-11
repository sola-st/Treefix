# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 20601
# GH 26314: Change ValueError to PerformanceWarning
class MockUnstacker(reshape_lib._Unstacker):
    def __init__(self, *args, **kwargs) -> None:
        # __init__ will raise the warning
        super().__init__(*args, **kwargs)
        raise Exception("Don't compute final result.")

with monkeypatch.context() as m:
    m.setattr(reshape_lib, "_Unstacker", MockUnstacker)
    df = DataFrame(
        {"ind1": np.arange(2**16), "ind2": np.arange(2**16), "count": 0}
    )

    msg = "The following operation may generate"
    with tm.assert_produces_warning(PerformanceWarning, match=msg):
        with pytest.raises(Exception, match="Don't compute final result."):
            df.pivot_table(
                index="ind1", columns="ind2", values="count", aggfunc="count"
            )
