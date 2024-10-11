# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
if (
    check_before_test
    and not raise_on_error
    and not can_connect(url, error_classes)
):
    pytest.skip(
        f"May not have network connectivity because cannot connect to {url}"
    )
try:
    exit(t(*args, **kwargs))
except Exception as err:
    errno = getattr(err, "errno", None)
    if not errno and hasattr(errno, "reason"):
        # error: "Exception" has no attribute "reason"
        errno = getattr(err.reason, "errno", None)  # type: ignore[attr-defined]

    if errno in skip_errnos:
        pytest.skip(f"Skipping test due to known errno and error {err}")

    e_str = str(err)

    if any(m.lower() in e_str.lower() for m in _skip_on_messages):
        pytest.skip(
            f"Skipping test because exception message is known and error {err}"
        )

    if not isinstance(err, error_classes) or raise_on_error:
        raise
    pytest.skip(f"Skipping test due to lack of connectivity and error {err}")
