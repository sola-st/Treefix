# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH#20601
# GH 26314: Change ValueError to PerformanceWarning

class MockUnstacker(reshape_lib._Unstacker):
    def __init__(self, *args, **kwargs) -> None:
        # __init__ will raise the warning
        super().__init__(*args, **kwargs)
        raise Exception("Don't compute final result.")

with monkeypatch.context() as m:
    m.setattr(reshape_lib, "_Unstacker", MockUnstacker)
    df = DataFrame(
        np.random.randn(2**16, 2),
        index=[np.arange(2**16), np.arange(2**16)],
    )
    msg = "The following operation may generate"
    with tm.assert_produces_warning(PerformanceWarning, match=msg):
        with pytest.raises(Exception, match="Don't compute final result."):
            df.unstack()
