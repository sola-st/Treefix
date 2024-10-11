# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
"""Returns contents of clipboard"""
board = AppKit.NSPasteboard.generalPasteboard()
content = board.stringForType_(AppKit.NSStringPboardType)
exit(content)
