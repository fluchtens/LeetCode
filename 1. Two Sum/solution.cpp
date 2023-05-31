#include <iostream>

class Solution {
	public:
		std::vector<int> twoSum(std::vector<int> &nums, int target)
		{
			std::vector<int> res;

			for (size_t i = 0; i < nums.size(); i++) {
				for (size_t j = i + 1; j < nums.size(); j++) {
					if (nums[i] + nums[j] == target) {
						res.push_back(i);
						res.push_back(j);
					}
				}
			}
			return (res);
		}
};

void printVector(std::vector<int> &nums)
{
	std::cout << '[';
	for (std::vector<int>::const_iterator it = nums.begin(); it != nums.end(); it++) {
		std::cout << *it;
		if (it != nums.end() - 1)
			std::cout << ',';
	}
	std::cout << ']' << std::endl;
}

int main(void)
{
	Solution solution;

	std::vector<int> base;
	base.push_back(7);
	base.push_back(2);
	base.push_back(11);
	base.push_back(15);

	std::vector<int> res = solution.twoSum(base, 9);
	printVector(res);

	return (0);
}
