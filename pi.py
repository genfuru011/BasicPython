text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

sentence = (
    "HOW I WANT A DRINK, ALCOHOLIC OF COURSE, AFTER THE HEAVY CHAPTERS INVOLVING "
    "QUANTUM MECHANICS. ALL OF THY GEOMETRY, HERR PLANCK, IS FAIRLY HARD."
)
sentence = sentence.replace(",", "").replace(".", "")

word_lengths = [len(word) for word in sentence.split()]

result = ''.join(map(str, word_lengths))

print(result)