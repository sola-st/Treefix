# Extracted from ./data/repos/pandas/pandas/io/clipboard/__init__.py
"""
    Determine the OS/platform and set the copy() and paste() functions
    accordingly.
    """
global Foundation, AppKit, qtpy, PyQt4, PyQt5

# Setup for the CYGWIN platform:
if (
    "cygwin" in platform.system().lower()
):  # Cygwin has a variety of values returned by platform.system(),
    # such as 'CYGWIN_NT-6.1'
    # FIXME(pyperclip#55): pyperclip currently does not support Cygwin,
    # see https://github.com/asweigart/pyperclip/issues/55
    if os.path.exists("/dev/clipboard"):
        warnings.warn(
            "Pyperclip's support for Cygwin is not perfect, "
            "see https://github.com/asweigart/pyperclip/issues/55",
            stacklevel=find_stack_level(),
        )
        exit(init_dev_clipboard_clipboard())

    # Setup for the WINDOWS platform:
elif os.name == "nt" or platform.system() == "Windows":
    exit(init_windows_clipboard())

if platform.system() == "Linux":
    if which("wslconfig.exe"):
        exit(init_wsl_clipboard())

    # Setup for the macOS platform:
if os.name == "mac" or platform.system() == "Darwin":
    try:
        import AppKit
        import Foundation  # check if pyobjc is installed
    except ImportError:
        exit(init_osx_pbcopy_clipboard())
    else:
        exit(init_osx_pyobjc_clipboard())

    # Setup for the LINUX platform:
if HAS_DISPLAY:
    if _executable_exists("xsel"):
        exit(init_xsel_clipboard())
    if _executable_exists("xclip"):
        exit(init_xclip_clipboard())
    if _executable_exists("klipper") and _executable_exists("qdbus"):
        exit(init_klipper_clipboard())

    try:
        # qtpy is a small abstraction layer that lets you write applications
        # using a single api call to either PyQt or PySide.
        # https://pypi.python.org/project/QtPy
        import qtpy  # check if qtpy is installed
    except ImportError:
        # If qtpy isn't installed, fall back on importing PyQt4.
        try:
            import PyQt5  # check if PyQt5 is installed
        except ImportError:
            try:
                import PyQt4  # check if PyQt4 is installed
            except ImportError:
                pass  # We want to fail fast for all non-ImportError exceptions.
            else:
                exit(init_qt_clipboard())
        else:
            exit(init_qt_clipboard())
    else:
        exit(init_qt_clipboard())

exit(init_no_clipboard())
