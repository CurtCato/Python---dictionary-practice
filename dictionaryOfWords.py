# Practice: Dictionary of Words
word_definitions = dict()
word_definitions["Awesome"] = "Curt"
word_definitions["Butthead"] = "Dustin"
word_definitions["FuckBoy"] = "Danny"
word_definitions["Mediocre Teacher"] = "Scott"

print(word_definitions["Awesome"], "is Awesome", word_definitions["Butthead"], "is a Butthead")

for (key, value) in word_definitions.items():
    print(f"The definition of {key} is {value}")

# Practice: English Idioms
idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

for (key, value) in idioms.items():
    s = " "
    sentence = s.join(value)
    print(f"{key} {sentence}")

# Challenge: Family Dictionary
my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
    "father": {
        "name": "Ray",
        "age": 72
    }
}

for fam_members, details in my_family.items():
    print(f"{details ['name']} is my {fam_members} and is {str(details['age'])} years old")

# fam_stuff = {v['name'] + " is my " + k + " and is " + str}