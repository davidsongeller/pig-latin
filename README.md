# pig-latin
Defines a list of consonant clusters called `lst` and then prompts the user to enter a sentence using the `input()` function. The sentence is then split into individual words using the `split()` function and stored in a list called `sentence`.

A `for` loop is then used to iterate over each word in the `sentence` list. The variable `P` is used to represent the index of the current word, and the variable `i` is used to represent the current word itself. 

- The first `if` checks if the word is a single letter and simply adds 'ay' to the end of the word. 
- The second `elif` checks if the word begins with a vowel and adds 'ay' to the end of the word. 
- The third `elif` checks if the first two letters of the word form a consonant cluster listed in `lst`, and if so, moves the consonant cluster to the end of the word and appends 'ay'. 
- The fourth `elif` checks if the word contains non-alphabetic characters and simply leaves the word unchanged. 
- Then the `else` statement applies the default Pig Latin transformation of moving the first consonant of the word to the end and appending 'ay'.

The `t()` function defined below `main()` is a helper function that returns the first two characters of a string, used for checking whether a word begins with a consonant cluster listed in `lst`.
