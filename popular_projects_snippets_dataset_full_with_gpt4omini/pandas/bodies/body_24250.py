# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
"""Copy string argument to clipboard"""
text = _stringifyText(text)  # Converts non-str values to str.
newStr = Foundation.NSString.stringWithString_(text).nsstring()
newData = newStr.dataUsingEncoding_(Foundation.NSUTF8StringEncoding)
board = AppKit.NSPasteboard.generalPasteboard()
board.declareTypes_owner_([AppKit.NSStringPboardType], None)
board.setData_forType_(newData, AppKit.NSStringPboardType)
