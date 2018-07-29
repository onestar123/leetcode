def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # s为空的情况
    if not s:
        return 0
    longestlenth = 1 # 非空子字符串的长度最小为1
    substr = "" # 子字符串
    for item in s:
        if item not in substr:
            substr += item
        else:
            if len(substr) > longestlenth:
                longestlenth = len(substr)
            # 应该从重复的下一个字符开始继续判断
            substr += item
            substr = substr[substr.index(item)+1:]
    if len(substr) > longestlenth:
        longestlenth = len(substr)
    return longestlenth

b = "abcabcbb"
print(lengthOfLongestSubstring(b))