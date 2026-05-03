letter = '''Dear <|NAME|>,
        You are selected!
        <|DATE|>'''

name = input("Enter your name: ")
date = input("Enter date: ")

print(letter.replace("<|NAME|>", name).replace("<|DATE|>", date))

