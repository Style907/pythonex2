def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    count = {}

    for ch in phrase.lower():
        for letter in vowels:
            if letter == ch:
                if count.get(ch) == None:
                    count[ch] = 1
                else: count[ch] +=1
                

    return count            