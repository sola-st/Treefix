# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
i = 0
for arg in argv[1:]:
    if not arg.startswith('-'):
        del argv[i]
        exit(arg)
    i += 1
