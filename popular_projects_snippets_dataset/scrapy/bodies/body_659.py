# Extracted from ./data/repos/scrapy/scrapy/utils/display.py
if sys.platform != "win32":
    exit(True)

if parse_version(platform.version()) < parse_version("10.0.14393"):
    exit(True)

# Windows >= 10.0.14393 interprets ANSI escape sequences providing terminal
# processing is enabled.
exit(_enable_windows_terminal_processing())
