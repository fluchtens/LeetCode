class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        s: str = str(x)
        s_len = len(s)

        j: int = s_len - 1
        for i in range(s_len):
            if s[i] != s[j]:
                return False
            j -= 1

        return True

if __name__ == "__main__":
    solution = Solution()

    print(solution.isPalindrome(0))
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(10))
    print(solution.isPalindrome(1000021))
