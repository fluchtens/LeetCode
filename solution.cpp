#include <iostream>

using namespace std;

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> result;

		for (int i = 0; i < nums.size(); i++) {
			for (int j = i + 1; j < nums.size(); j++) {
				if (nums[i] + nums[j] == target) {
					result.push_back(i);
					result.push_back(j);
					return result;
				}
			}
		}

        return (result);
    }
};

int main(void)
{
	std::vector<int> inputVector;
	inputVector.push_back(3);
	inputVector.push_back(2);
	inputVector.push_back(3);

	Solution Solution;
	std::vector<int> result = Solution.twoSum(inputVector, 8);

	std::cout << '[';
	for (std::vector<int>::iterator it = result.begin(); it != result.end(); it++) {
		std::cout << *it;
		if (it != result.end() - 1) {
			std::cout << ", ";
		}
	}
	std::cout << ']' << std::endl;

	return (0);
}
