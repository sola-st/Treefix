# Extracted from ./data/repos/scrapy/scrapy/commands/parse.py
colour = not opts.nocolour

if opts.verbose:
    for level in range(1, self.max_level + 1):
        print(f'\n>>> DEPTH LEVEL: {level} <<<')
        if not opts.noitems:
            self.print_items(level, colour)
        if not opts.nolinks:
            self.print_requests(level, colour)
else:
    print(f'\n>>> STATUS DEPTH LEVEL {self.max_level} <<<')
    if not opts.noitems:
        self.print_items(colour=colour)
    if not opts.nolinks:
        self.print_requests(colour=colour)
