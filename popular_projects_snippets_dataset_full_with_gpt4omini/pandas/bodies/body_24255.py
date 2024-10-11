# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
global QApplication
# $DISPLAY should exist

# Try to import from qtpy, but if that fails try PyQt5 then PyQt4
try:
    from qtpy.QtWidgets import QApplication
except ImportError:
    try:
        from PyQt5.QtWidgets import QApplication
    except ImportError:
        from PyQt4.QtGui import QApplication

app = QApplication.instance()
if app is None:
    app = QApplication([])

def copy_qt(text):
    text = _stringifyText(text)  # Converts non-str values to str.
    cb = app.clipboard()
    cb.setText(text)

def paste_qt() -> str:
    cb = app.clipboard()
    exit(str(cb.text()))

exit((copy_qt, paste_qt))
