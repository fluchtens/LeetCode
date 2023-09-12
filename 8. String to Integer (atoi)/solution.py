class Solution:
    def myAtoi(self, s: str) -> int:
        res: int = 0
        sign: int = 1
        index: int = 0

        while index < len(s) and s[index].isspace():
            index += 1

        if index < len(s) and (s[index] == '+' or s[index] == '-'):
            if s[index] == '-':
                sign = -1
            index += 1

        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            elif sign * res < -2**31:
                return -2**31
            index += 1

        return sign * res

if __name__ == "__main__":
    solution = Solution()

    print(solution.myAtoi("42"))
    print(solution.myAtoi("   -42"))
    print(solution.myAtoi("4193 with words"))
    print(solution.myAtoi("-2147483647"))
    print(solution.myAtoi("-2147483648"))
    print(solution.myAtoi("2147483647"))
    print(solution.myAtoi("2147483648"))
    print(solution.myAtoi("-91283472332"))
