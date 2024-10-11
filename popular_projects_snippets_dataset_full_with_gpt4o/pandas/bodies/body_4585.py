# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
with monkeypatch.context() as m:
    m.setattr(nanops, "_USE_BOTTLENECK", False)
    exit()
