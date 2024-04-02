class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.strip()
        str_len: int = len(new_str)
        index: int = str_len - 1
        final_str: str = ""

        while index >= 0:
            if not new_str[index].isspace():
                final_str = new_str[index] + final_str
            else:
                break
            index = index - 1

        return len(final_str)


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))
