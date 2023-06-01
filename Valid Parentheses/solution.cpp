#include <iostream>

class Solution
{
	private:
		bool _isBracketsClosed(std::string &str, char open, char close)
		{
			int count = 0;

			for (size_t i = 0; i < str.length(); i++) {
				if (str[i] == open) {
					count++;
				}
				if (str[i] == close) {
					if (count == 0) {
						return (false);
					}
					count--;
				}
			}
			if (count != 0) {
				return (false);
			}
			return (true);
		}

	public:
		bool isValid(std::string str)
		{
			if (this->_isBracketsClosed(str, '(', ')') == false) {
				return (false);
			} else if (this->_isBracketsClosed(str, '[', ']') == false) {
				return (false);
			} else if (this->_isBracketsClosed(str, '{', '}') == false) {
				return (false);
			} else {
				return (true);
			}
		}
};

int main(void)
{
	Solution solution;

	std::cout << solution.isValid("()") << std::endl;
	std::cout << solution.isValid("()[]{}") << std::endl;
	std::cout << solution.isValid("(]") << std::endl;

	return (0);
}
