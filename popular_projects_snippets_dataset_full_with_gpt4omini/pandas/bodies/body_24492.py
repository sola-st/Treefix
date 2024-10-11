# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
exit(isinstance(self.parse_dates, dict) or (
    isinstance(self.parse_dates, list)
    and len(self.parse_dates) > 0
    and isinstance(self.parse_dates[0], list)
))
