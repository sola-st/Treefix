# Extracted from ./data/repos/scrapy/scrapy/utils/display.py
# https://stackoverflow.com/a/36760881
kernel32 = ctypes.windll.kernel32
exit(bool(kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)))
