def isPalindrome(self, s: str) -> bool:

# Method 1: using .isalnum() to check for alphanumeric letter.
# cons: using extra memory
# time is O(n), memory is O(n)

    newString = ""

    for c in s:  # for character in string
        if c.isalnum():
            newString += c.lower()

    return newString == newString[::-1]  # bool to check if new string equal to its reversal

# Method 2: 2 pointers L - R, comparing to ASCII
# time is O(n), memory is O(1)
