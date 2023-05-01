### Description
This script takes a sentence as input from the user and converts it into pig latin. It follows the following rules:

- If a word starts with a vowel, add 'ay' to the end of the word.
- If a word starts with a consonant, move the consonant to the end of the word and add 'ay'.
- If a word starts with a consonant cluster, move the cluster to the end of the word and add 'ay'.
- If a word has non-alphabetic characters, keep it as it is.

### Functionality
The script contains one main function, main(), which performs the following actions:

1. Initializes a list of consonant clusters.
2. Takes a sentence as input from the user.
3. Splits the sentence into individual words.
4. Iterates over each word in the sentence and applies the pig latin conversion rules.
5. Joins the converted words back into a sentence and returns it.
The script also contains a helper function, t(str), which returns the first two characters of a string.

### Usage
1. Run the script.
2. Enter a sentence when prompted.
3. The script will output the pig latin version of the sentence.
### Improvements
Add error handling for cases where the user enters invalid input (e.g. a number instead of a sentence).
Add unit tests to ensure the script is working correctly.
Refactor the code to improve readability and maintainability.
