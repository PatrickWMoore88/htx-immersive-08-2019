#Exercise 1
phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}
#1
print(phonebook_dict['Elizabeth'])
#2
phonebook_dict['Kareem'] = '938-489-1234'
#3
del phonebook_dict['Alice']
#4
phonebook_dict['Bob'] = '968-345-2345'
#5
print(phonebook_dict)
print('=======================================================')
#Exercise 2: Nested Dictionaries
ramit = { 
  'name': 'Ramit', 
  'email': 'ramit@gmail.com', 
  'interests': ['movies', 'tennis'], 
  'friends': [ 
     { 
       'name': 'Jasmine', 
       'email': 'jasmine@yahoo.com', 
       'interests': ['photography', 'tennis']
     }, 
     { 
        'name': 'Jan', 
        'email': 'jan@hotmail.com', 
        'interests': ['movies', 'tv'] 
     } 
    ] 
}
#1
print(ramit['email'])
#2
print(ramit['interests'][0])
#3
print(ramit['friends'][0]['email'])
#4
print(ramit['friends'][1]['interests'][1])
print('=======================================================')
#Exercise 3: Letter Summary
word = str(input("What is your word?: "))
letters_in_word = {}
val = 1
for letter in word:
    if letter in word:
        letters_in_word[str(letter)] = val * word.count(str(letter))
print(letters_in_word)
print('=======================================================')
#Exercise 4: Word Summary + Bonus Challenge
phrase = str(input("What is your phrase?: "))
words_in_phrase = {}
val = 1
for word in phrase.split():
    if word in phrase:
        words_in_phrase[str(word)] = val * phrase.count(str(word))
print(words_in_phrase)
three_highest = sorted(words_in_phrase.items(), key = lambda x:-x[1])[:3]
for x in three_highest:
  print("{0}: {1}".format(*x))

 
