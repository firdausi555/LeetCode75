class Solution:
    def reverseVowels(self, s):
        check=[i for i in s if i in "AEIOUaeiou"]
        result =[i if i not in "AEIOUaeiou" else check.pop() for i in s]
        return "".join(result)
        
