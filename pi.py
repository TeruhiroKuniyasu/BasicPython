text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

words = text.split()

lengths = [len(word.strip(",.")) for word in words]

string = ''.join(map(str, lengths))

print(string)
