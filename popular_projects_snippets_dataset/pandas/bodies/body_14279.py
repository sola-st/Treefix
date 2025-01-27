# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_printing.py
# GH 10491
formatters = ip.instance(config=ip.config).display_formatter.formatters
mimetype = "application/vnd.dataresource+json"

with pd.option_context("display.html.table_schema", True):
    assert "application/vnd.dataresource+json" in formatters
    assert formatters[mimetype].enabled

# still there, just disabled
assert "application/vnd.dataresource+json" in formatters
assert not formatters[mimetype].enabled

# able to re-set
with pd.option_context("display.html.table_schema", True):
    assert "application/vnd.dataresource+json" in formatters
    assert formatters[mimetype].enabled
    # smoke test that it works
    ip.instance(config=ip.config).display_formatter.format(cf)
