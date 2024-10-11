# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
def copy_osx_pyobjc(text):
    """Copy string argument to clipboard"""
    text = _stringifyText(text)  # Converts non-str values to str.
    newStr = Foundation.NSString.stringWithString_(text).nsstring()
    newData = newStr.dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
    board = AppKit.NSPasteboard.generalPasteboard()
    board.declareTypes_owner_([AppKit.NSStringPboardType], None)
    board.setData_forType_(newData, AppKit.NSStringPboardType)

def paste_osx_pyobjc():
    """Returns contents of clipboard"""
    board = AppKit.NSPasteboard.generalPasteboard()
    content = board.stringForType_(AppKit.NSStringPboardType)
    exit(content)

exit((copy_osx_pyobjc, paste_osx_pyobjc))
