#include <iostream>

class Solution
{
	public:
		int myAtoi(std::string str)
		{
			long long res = 0;
			int sign = 1;
			int i = 0;

			while ((str[i] >= 9 && str[i] <= 13) || str[i] == 32) {
				i++;
			}
			if (str[i] == '+' || str[i] == '-') {
				if (str[i] == '-')
					sign = -1;
				i++;
			}
			while (std::isdigit(str[i])) {
				res = (res * 10) + (str[i] - '0');
				if (sign * res < INT_MIN)
					return (INT_MIN);
				if (sign * res > INT_MAX)
					return (INT_MAX);
				i++;	
			}
			return (sign * res);
		}
};

int main(void)
{
	Solution solution;

	std::cout << solution.myAtoi("42") << std::endl;
	std::cout << solution.myAtoi("   -42") << std::endl;
	std::cout << solution.myAtoi("4193 with words") << std::endl;

	std::cout << solution.myAtoi("-2147483647") << std::endl;
	std::cout << solution.myAtoi("-2147483648") << std::endl;

	std::cout << solution.myAtoi("2147483647") << std::endl;
	std::cout << solution.myAtoi("2147483648") << std::endl;

	return (0);
}
