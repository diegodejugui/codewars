def permute_a_palindrome(input): 
    
    return len(input) - len(list(filter(lambda c : input.count(c) % 2 == 0, input)))
