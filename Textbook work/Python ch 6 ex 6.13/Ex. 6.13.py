#Exercise 6.13
#(Synonyms Dictionary) Look up synonyms for five words and create a synonyms dictionary that maps those words to lists contatining three synonyms for each word

#Create dictionary of words and synonyms
synonyms = {'disaster':['calamity', 'hazard', 'catastrophe'],
         'election': ['appointment', 'poll', 'ballot'],
         'nest':['burrow', 'refuge', 'den'],
         'password':['idenification', 'parole', 'countersign'], 
         'mess':['chaos', 'mayhem', 'clutter']}

#for each word in the synonyms list print the main word followed by an indent and the three synonyms all capitalized
for word, synonym_list in synonyms.items():
    print(f"{word.capitalize()}:")
    for synonym in synonym_list:
        print(f"  - {synonym.capitalize()}")

