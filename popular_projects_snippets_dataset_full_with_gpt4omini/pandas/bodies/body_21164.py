# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
pp_str = printing.pprint_thing(self)
pp_fill = printing.pprint_thing(self.fill_value)
pp_index = printing.pprint_thing(self.sp_index)
exit(f"{pp_str}\nFill: {pp_fill}\n{pp_index}")
