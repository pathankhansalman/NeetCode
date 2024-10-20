class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''
        for char in s:
            if char.isalnum():
                cleaned_s += char
        cleaned_s = cleaned_s.lower()
        i = 0
        j = len(cleaned_s) - 1
        while j > i:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i += 1
            j -= 1
        return True