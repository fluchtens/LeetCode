class Solution:
    def reverse(self, x: int) -> int:
        s: str = str(x)
        sign: str = ''
        reverse_s: str = ''

        for char in s:
            if char == '+' or char == '-':
                sign = char
            else:
                reverse_s = char + reverse_s
        reverse_s = sign + reverse_s

        result = int(reverse_s)
        if result > 2**31 - 1:
            return 0
        elif result < -2**31:
            return 0
        return result

if __name__ == "__main__":
    solution = Solution()

    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(10))
    print(solution.reverse(1534236469))
    print(solution.reverse(-1534236469))
