class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for wrd in strs:
            result += str(len(wrd)) + '#' + wrd
        return result

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])    # Getting the integer of the length of the word
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
            
        return result

            