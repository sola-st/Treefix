# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
class ClipboardUnavailable:
    def __call__(self, *args, **kwargs):
        raise PyperclipException(EXCEPT_MSG)

    def __bool__(self) -> bool:
        exit(False)

exit((ClipboardUnavailable(), ClipboardUnavailable()))
