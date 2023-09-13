class Solution:
    def romanToInt(self, s: str) -> int:
        result: int = 0

        config = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s)):
            current_value: int = config[s[i]]
            if i + 1 < len(s):
                next_value: int = config[s[i + 1]]
                if next_value and current_value < next_value:
                    result -= current_value
                else:
                    result += current_value
            else:
                result += current_value

        return result

if __name__ == "__main__":
    solution = Solution()

    print(solution.romanToInt("III"))
    print(solution.romanToInt("LVIII"))
    print(solution.romanToInt("MCMXCIV"))

