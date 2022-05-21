dictionary = {"English": ["mine", "yours", "a little", "english", "all of it", "drip", " love you", "i hate you",],
    "Sheng": ["wangu", "yako", "kiasi", "kizungu", "zote",  "luku", "nakulove", "nakuhate", ],
    "Shembeteng": ["wambatangu", "yambatako", "kiambatasi", "kizambatangu", "zombotote", "lukumbatangu", "nakulombotove", "nakuhambatate",],
}

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(key, ":", value)


print_dictionary(dictionary)


def translate(phrase, input_language, output_language):
    if input_language == output_language:
        return phrase
    else:
        return dictionary[output_language][dictionary[input_language].index(phrase)]

phrase = input(
    "Enter a phrase: "
)  # The dictionary is small -> Use the exact words in it
input_language = input("Enter the input language: ")
output_language = input("Enter the output language: ")

print(
    f"You entered: {phrase} in {input_language} and you want to translate it to {output_language}"
)
print(f"The translation is: {translate(phrase, input_language, output_language)}")
