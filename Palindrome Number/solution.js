/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  const xStr = x.toString();
  let j = xStr.length - 1;

  for (let i = 0; i < xStr.length; i++) {
    if (xStr[i] !== xStr[j]) {
      return false;
    }
    j--;
  }
  return true;
};
