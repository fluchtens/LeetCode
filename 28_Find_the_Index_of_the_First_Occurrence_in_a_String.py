class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        final_string: str = ""
        final_index: int = -1

        i: int = 0
        while (i < len(haystack)):
            j: int = 0
            matched_string: str = ""
            matched_index = 0
            next_index = -1

            while (i < len(haystack) and j < len(needle) and haystack[i] == needle[j]):
                if (j == 0):
                    matched_index = i
                    next_index = i
                matched_string += haystack[i]
                j = j + 1
                i = i + 1
            if (len(matched_string) > len(final_string)):
                final_string = matched_string
                final_index = matched_index
            if (next_index >= 0):
                i = next_index
            i = i + 1

        if (final_string != needle):
            final_index = -1
        return final_index
