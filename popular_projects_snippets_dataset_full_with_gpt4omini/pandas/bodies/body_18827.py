# Extracted from ./data/repos/pandas/pandas/_testing/_warnings.py
"""Assert that no extra warnings apart from the expected ones are caught."""
extra_warnings = []

for actual_warning in caught_warnings:
    if _is_unexpected_warning(actual_warning, expected_warning):
        # GH#38630 pytest.filterwarnings does not suppress these.
        if actual_warning.category == ResourceWarning:
            # GH 44732: Don't make the CI flaky by filtering SSL-related
            # ResourceWarning from dependencies
            unclosed_ssl = (
                "unclosed transport <asyncio.sslproto._SSLProtocolTransport",
                "unclosed <ssl.SSLSocket",
            )
            if any(msg in str(actual_warning.message) for msg in unclosed_ssl):
                continue
            # GH 44844: Matplotlib leaves font files open during the entire process
            # upon import. Don't make CI flaky if ResourceWarning raised
            # due to these open files.
            if any("matplotlib" in mod for mod in sys.modules):
                continue

        extra_warnings.append(
            (
                actual_warning.category.__name__,
                actual_warning.message,
                actual_warning.filename,
                actual_warning.lineno,
            )
        )

if extra_warnings:
    raise AssertionError(f"Caused unexpected warning(s): {repr(extra_warnings)}")
