# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
try:
    import_optional_dependency("pytest_asyncio")
    async_mark = pytest.mark.asyncio
except ImportError:
    async_mark = pytest.mark.skip(reason="Missing dependency pytest-asyncio")

exit(async_mark)
