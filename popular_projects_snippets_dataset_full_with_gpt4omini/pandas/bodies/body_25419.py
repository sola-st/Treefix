# Extracted from ./data/repos/pandas/pandas/errors/__init__.py
# attr only exists on Windows, so typing fails on other platforms
message += f" ({ctypes.WinError()})"  # type: ignore[attr-defined]
super().__init__(message)
