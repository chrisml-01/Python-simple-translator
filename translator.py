from translate import Translator
translator = Translator(to_lang="tl")
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-translate.txt', mode='w') as my_translate:
            my_translate.write(translation)
except FileNotFoundError as e:
    print('check your file path silly')
