'''
Given an input of a dictionary of words and an input string that does not contain spaces, 
write a method that returns a string with spaces inserted accordingly.

•	The same word in the dictionary may be reused multiple times in the segmentation.
•	You may assume the dictionary does not contain duplicate words.
•	If there are leftover characters in the string return null/none


Examples:
Input: "bloombergisfun", ["bloom","bloomberg","is","fun"]
Output: "bloomberg is fun"

Input: "bloombergisfun", ["bloom", "bloomberg","is"]
Output: None/Null

Input: "bloombergisfun", ["bloom", "berg", "bloomberg","is","fun"]
Output: "bloom berg is fun"
'''


def spacedString(input:str, wordList: list[str]):
    # use Set for O(1) time complexity
    wordSet = set(wordList)
    memo = {}

    # define recursive function
    def helper(s:str):
        if s in memo:
            return memo[s]

        result = str('')
        for i in range(len(s)):
            word = s[:i+1]
            if word in wordSet:
                if word != s:
                    restOfWord = helper(s[i+1:])
                    if restOfWord:
                        result += word + " " + restOfWord

                else:
                    result += word
        memo[s] = result       
        return result
    
    return helper(input)    



#Examples:
a = spacedString("bloombergisfun", ["bloom","bloomberg","is","fun"]) # Output: "Bloomberg is fun"
print(a)

b = spacedString("bloombergisfun", ["bloom", "bloomberg","is"]) #Output: None
print(b)

c = spacedString("bloombergisfun", ["bloom", "berg", "bloomberg","is","fun"]) #Output bloomberg is fun
print(c)