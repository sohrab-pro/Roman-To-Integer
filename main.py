class Solution:
    def romanToInt(self, s: str) -> int:
        base_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        special_cases = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        num = 0
        index = 0
        while index < len(s):
            if index + 1 < len(s) and s[index:index+2] in special_cases:
                num += special_cases[s[index:index+2]]
                index += 2
            else:
                num += base_values[s[index]]
                index += 1

        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))
