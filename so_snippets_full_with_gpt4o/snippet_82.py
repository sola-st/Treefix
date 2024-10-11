# Extracted from https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-represents-a-number-float-or-int
word = "1.1"

"".join(word.split(".")).isnumeric()
True

word = "1.1"

"".join(word.split(".")).isdigit()
True

word = "1.1"

"".join(word.split(".")).isdecimal()
True

%timeit "".join(word.split(".")).isnumeric()
257 ns ± 12 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit "".join(word.split(".")).isdigit()
252 ns ± 11 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%timeit "".join(word.split(".")).isdecimal()
244 ns ± 7.17 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

