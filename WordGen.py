from numpy import random 

#def that returns a random integer taken from the normal distribution of 
#word length:
def word_length(): 
    x = 0
    while x < 3 or x > 23: #keeps rolling until it gets an actual valid no.
        x = round(random.normal(loc=7.6, scale=3))
        #chooses number from normal distribution of mean 7.6 and s.d. 3

    return x


def word_gen(num_letter): #num_letters is the number of letters wanted 

    number_letters = num_letter # chooses how long the name is
    counter = 0 #keeps track of loop

    vowels = ["a", "e", "i", "o", "u"] #to avoid getting multiple vowels one after another later on in the code

    final_word = [] # array that returns end result

    vow_or_not_cache = [] #to check not too many consonants follow each other

    while counter < num_letter: #create spaces for 

        final_word.append("")
        vow_or_not_cache.append("")
        counter += 1
        
    counter = 0 

    while counter < number_letters:

        vow_or_not = random.randint(1,2) # if 1 then vowel if 2 then letter
        vow_or_not_cache[counter] = vow_or_not #save number selected

        if vow_or_not_cache[-1] == vow_or_not_cache[-2] and vow_or_not_cache[-2] == vow_or_not_cache[-3]: #if last 3 letters selected were all consonants or vowels, change type of letter
            if vow_or_not == 1:
                vow_or_not = 2
            elif vow_or_not == 2:
                vow_or_not = 1
            else:
                vow_or_not_cache.append(vow_or_not)

  
        # following probabilities are approximated values of the ones shown on the website:  http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html

        if vow_or_not == 1: # vowel was chosen in this case

            prob_l = random.randint(0,38) #choose vowel at random

            if prob_l < 13:
                new_l = "e"
            elif 13 <= prob_l and prob_l < 21:
                new_l = "a"
            elif 21 <= prob_l and prob_l < 29:
                new_l = "o"
            elif 29 <= prob_l and prob_l < 36:
                new_l = "i"
            elif 36 <= prob_l :
                new_l = "u"
            else:
                next
        else: #meaning letters in this case
            prob_l = random.randint(0,51) #choose consonant at random
            if  prob_l < 10:
                new_l = "t"
            elif 10 <= prob_l and prob_l < 17:
                new_l = "n"
            elif 17 <= prob_l and prob_l < 23:
                new_l = "s"
            elif 23 <= prob_l and prob_l < 29:
                new_l = "r"
            elif 29 <= prob_l and prob_l < 33:
                new_l = "d"
            elif 33 <= prob_l and prob_l < 37:
                new_l = "l"
            elif 37 <= prob_l and prob_l < 40:
                new_l = "c"
            elif 40 <= prob_l and prob_l < 43:
                new_l = "m"
            elif 43 <= prob_l and prob_l < 45:
                new_l = "f"
            elif 45 <= prob_l and prob_l < 47:
                new_l = "g"
            elif 47 <= prob_l and prob_l < 49:
                new_l = "p"
            elif prob_l == 49:
                new_l = "b"
            elif prob_l == 50:
                new_l = "v"
            elif prob_l == 51:
                low_prob_letters = random.randint(1,8)  # z has vey low probability (0.07%) therefore this could be a way to simulate it, though actual probability needs to be worked out. Here can be added the missing letters as well, if necessary.
                if low_prob_letters <= 6:
                    new_l = "k"
                else:
                    new_l = "z"
            else: 
                next
            # missing letters are: y, w, x, q (very low percentages and specific letters) and h (difficult to use in simulating syllables) 

        
        if new_l != final_word[counter-1] and new_l != final_word[counter-2]: #adds letter to list only 
            final_word[counter] = new_l
            counter += 1



    final_word_str = "".join(final_word) # turn array to string 
    return final_word_str


#NOTE TO SELF: Instead of adding to the list the chosen letters, this version of the generation replaces already occupied spaces (lists need to be filled in advance to avoid range error). Hence, it can only generate words of legth == to the number of elements in final_word. Adding elements to this list will make it so it is able to produce longer words. 
#same applied for vow_or_not_cache

#NOTE TO MIHI: my annotations come from the ruby version. Pretend "array" = "list"