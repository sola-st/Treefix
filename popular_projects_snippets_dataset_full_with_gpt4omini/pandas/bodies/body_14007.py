# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_console.py
# GH 21552
with monkeypatch.context() as context:
    context.setattr("locale.getpreferredencoding", lambda: "foo")
    context.setattr("sys.stdout", MockEncoding(encoding))
    assert detect_console_encoding() == "foo"
