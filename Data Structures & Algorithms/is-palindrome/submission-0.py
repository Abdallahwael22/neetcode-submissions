class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join([i for i in s if i.isalnum()])
        s=s.lower()
        rs="".join(reversed(s))
        print(f"s: {s}")
        print(f"rs: {rs}")
        return s==rs