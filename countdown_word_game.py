from multiset import Multiset

import wordfreq

words = wordfreq.iter_wordlist('en')
#givenletters = Multiset(list('redaardvark'))

givenletters = Multiset(list(input("Enter given letters: ").strip()))

#words = map(str.strip, open('/usr/share/dict/words').readlines() )
#words = map(str.lower, words)



found_words_dict = {}
for word in words:
        if Multiset(list(word))<=givenletters:
            l = len(word)
            if l not in found_words_dict:
                found_words_dict[l] = [word]
            else:
                found_words_dict[l].append(word)

print("Given letters:")
print(givenletters)
print()
                
for k in sorted(found_words_dict):
    found_words_dict[k].sort(reverse=True,key=(lambda w: wordfreq.word_frequency(w,'en')))
    print('%d letter words:'%(k,))
    print(found_words_dict[k])
    print()
    
                          

