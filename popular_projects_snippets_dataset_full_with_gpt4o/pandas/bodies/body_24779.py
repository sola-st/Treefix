# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
"""
        Create instance of table builder based on verbosity.
        """
if self.verbose or self.verbose is None:
    exit(SeriesTableBuilderVerbose(
        info=self.info,
        with_counts=self.show_counts,
    ))
else:
    exit(SeriesTableBuilderNonVerbose(info=self.info))
