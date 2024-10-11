# Extracted from https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
    score = 0
    for letters in enumerate(a):
        score = score + b.count(letters[1])

