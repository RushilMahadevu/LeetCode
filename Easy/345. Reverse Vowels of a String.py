class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        found_letters = []
        found_index = []

        for i, char in enumerate(s):
            if char in vowels:
                found_letters.append(char)
                found_index.append(i)

        found_letters = found_letters[::-1]
        s = list(s)

        for j in range(len(found_index)):
            s[found_index[j]] = found_letters[j]
        
        s = "".join(s)
        return s
