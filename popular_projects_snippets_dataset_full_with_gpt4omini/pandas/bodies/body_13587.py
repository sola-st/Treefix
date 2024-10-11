# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
msg = "`position_float` should be one of 'raggedright', 'raggedleft', 'centering',"
with pytest.raises(ValueError, match=msg):
    styler.to_latex(position_float="bad_string")

msg = "`position_float` cannot be used in 'longtable' `environment`"
with pytest.raises(ValueError, match=msg):
    styler.to_latex(position_float="centering", environment="longtable")
