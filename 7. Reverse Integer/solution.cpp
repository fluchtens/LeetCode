#include <iostream>
#include <sstream>

class Solution
{
	public:
		int reverse(int x)
		{
			std::string str = std::to_string(x);
			std::string reverseStr;
			int len = str.length();

			for (int i = 0; i < len; i++) {
				if (str[i] == '+' || str[i] == '-') {
					reverseStr.push_back(str[i]);
					len++;
					i++;
				}
				reverseStr.push_back(str[len - 1 - i]);
			}

			long long res = std::stoll(reverseStr);
			if (res < std::numeric_limits<int>::min()) {
				return (0);
			}
			if (res > std::numeric_limits<int>::max()) {
				return (0);
			}
			return (static_cast<int>(res));
		}
};

int main(void)
{
	Solution solution;

	std::cout << solution.reverse(123) << std::endl;
	std::cout << solution.reverse(-123) << std::endl;
	std::cout << solution.reverse(120) << std::endl;
	std::cout << solution.reverse(10) << std::endl;
	std::cout << solution.reverse(1534236469) << std::endl;

	return (0);
}
