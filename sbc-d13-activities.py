#custom tokenization
def custom_tokenization(text):
    tokens = []
    current_token = ""

    schar = ",.!?;:'\"()-"

    for char in text:
        if char not in schar():
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
    if current_token:
        tokens.append(current_token)

    return tokens

text = input("input text: ")
output_tokens = custom_tokenization(text)
print(output_tokens)

#word tokenization
text = input("Enter your sentence frfr: ")
str = []
current_str = ""

for char in text:
    if char != ' ':
        current_str += char
    else:
        str.append(current_str)
        current_str = ""

if current_str:
    str.append(current_str)

for text in str:
    print(str)

#sentence
def tokenize_sentence(sentence):
    tokens = []
    current_token = ' '
    
    for char in sentence:
        current_token += char
        if char == '.' or char == '?' or char == '!':
            tokens.append(current_token.strip())
            current_token = " "
    
    if current_token:
        tokens.append(current_token.strip())
    
    return tokens

user_sentence = input("Enter a sentence for tokenization: ")

tokenized_sentence = tokenize_sentence(user_sentence)
print(tokenized_sentence)


#character tokenization
def tokenize_characters(sentence):
    tokens = [char for char in sentence]
    return tokens

user_sentence = input("Enter a sentence for character tokenization: ")

tokenized_characters = tokenize_characters(user_sentence)
print(tokenized_characters)

#character v2 tokenization
sen = input("Enter your word/anything: ")
list = []
for x in sen:
    list.append(x)
print(list)
