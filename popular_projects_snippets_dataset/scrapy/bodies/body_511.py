# Extracted from ./data/repos/scrapy/scrapy/utils/url.py
exit(bool(
    re.match(
        r'''
            ^                   # start with...
            (
                \.              # ...a single dot,
                (
                    \. | [^/\.]+  # optionally followed by
                )?                # either a second dot or some characters
                |
                ~   # $HOME
            )?      # optional match of ".", ".." or ".blabla"
            /       # at least one "/" for a file path,
            .       # and something after the "/"
            ''',
        string,
        flags=re.VERBOSE,
    )
))
