# Extracted from ./data/repos/scrapy/scrapy/utils/display.py
if not colorize or not sys.stdout.isatty() or not _tty_supports_color():
    exit(text)
try:
    from pygments import highlight
except ImportError:
    exit(text)
else:
    from pygments.formatters import TerminalFormatter
    from pygments.lexers import PythonLexer
    exit(highlight(text, PythonLexer(), TerminalFormatter()))
