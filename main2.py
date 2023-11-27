def isPalindrome(self, s: str) -> bool:

# Method 2: 2 pointers L - R,
# time is O(n), memory is O(1)

    l, r = 0, len(s) - 1  # setting starting position for the two ends

    while l < r:
        # checking from L -> R then R -> L for alphanum's, if not, increment or decrement by 1 letter
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():  # if 2 letters do not match >> not palindrome
            return False
        l, r = l + 1, r - 1
    return True


# create helper func alphaNum() comparing to ASCII via ord()
def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


# errorr: "NameError: name 'alphaNum' is not defined"