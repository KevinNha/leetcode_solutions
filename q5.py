from datetime import datetime

class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = (1, s[0])

        if len(s) == 1:
            return s
        for index, letter in enumerate(s):
            longest = self.get_longest(s, index - 1, index + 1, letter, longest)

            if index + 1 < len(s) and s[index + 1] == letter:
                palindrome_length = 2
                if palindrome_length > longest[0]:
                    longest = (palindrome_length, letter + letter)
                longest = self.get_longest(s, index - 1, index + 2, letter + letter, longest)
        return longest[1]

    def get_longest(self, string, left, right, start_letter, longest):
        palindrome_length = len(start_letter)
        palindrome_pattern = start_letter
        while left >= 0 and right < len(string):
            if string[left] == string[right]:
                palindrome_length += 2
                palindrome_pattern = string[left] + palindrome_pattern + string[left]
                if palindrome_length > longest[0]:
                    longest = (palindrome_length, palindrome_pattern)
                left -= 1
                right += 1
            else:
                return longest
        return longest
        
# Need to figure out whether palindrome or not first
# Check if it can go left or not
# Each letter basically needs to check through two possibilities:
#   1. using the letter as the center point
#   2. using the letter and the right letter as the center point
# baaabb

if __name__ == '__main__':
    solution = Solution()
    before = datetime.now()
    print(solution.longestPalindrome("dqmvxouqesajlmksdawfenyaqtnnfhmqbdcniynwhuywucbjzqxhofdzvposbegkvqqrdehxzgikgtibimupumaetjknrjjuygxvncvjlahdbibatmlobctclgbmihiphshfpymgtmpeneldeygmzlpkwzouvwvqkunihmzzzrqodtepgtnljribmqneumbzusgppodmqdvxjhqwqcztcuoqlqenvuuvgxljcnwqfnvilgqrkibuehactsxphxkiwnubszjflvvuhyfwmkgkmlhmvhygncrtcttioxndbszxsyettklotadmudcybhamlcjhjpsmfvvchduxjngoajclmkxiugdtryzinivuuwlkejcgrscldgmwujfygqrximksecmfzathdytauogffxcmfjsczaxnfzvqmylujfevjwuwwaqwtcllrilyncmkjdztleictdebpkzcdilgdmzmvcllnmuwpqxqjmyoageisiaeknbwzxxezfbfejdfausfproowsyyberhiznfmrtzqtgjkyhutieyqgrzlcfvfvxawbcdaawbeqmzjrnbidnzuxfwnfiqspjtrszetubnjbznnjfjxfwtzhzejahravwmkakqsmuynklmeffangwicghckrcjwtusfpdyxxqqmfcxeurnsrmqyameuvouqspahkvouhsjqvimznbkvmtqqzpqzyqivsmznnyoauezmrgvproomvqiuzjolejptuwbdzwalfcmweqqmvdhejguwlmvkaydjrjkijtrkdezbipxoccicygmmibflxdeoxvudzeobyyrutbcydusjhmlwnfncahxgswxiupgxgvktwkdxumqp"))
    after = datetime.now()
    print("Function execution time: ", after - before)