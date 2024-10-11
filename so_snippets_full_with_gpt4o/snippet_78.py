# Extracted from https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
'   spacious   '.rstrip()
'   spacious'
"AABAA".rstrip("A")
  'AAB'
"ABBA".rstrip("AB") # both AB and BA are stripped
   ''
"ABCABBA".rstrip("AB")
   'ABC'

