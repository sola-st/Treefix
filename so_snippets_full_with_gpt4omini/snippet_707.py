# Extracted from https://stackoverflow.com/questions/6903557/splitting-on-first-occurrence
text = "123mango abcd mango kiwi peach"

text.partition("mango")
('123', 'mango', ' abcd mango kiwi peach')

text.partition("mango")[-1]
' abcd mango kiwi peach'

text.partition("mango")[-1].lstrip()  # if whitespace strip-ing is needed
'abcd mango kiwi peach'

(<pre>, <separator>, <post>)

