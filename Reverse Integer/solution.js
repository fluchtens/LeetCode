/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const INT_MIN = Math.pow(-2, 31);
  const INT_MAX = Math.pow(2, 31);
  const xStr = x.toString();
  const len = xStr.length;
  let newStr = "";

  for (let i = len - 1; i >= 0; i--) {
    if (i === 0 && xStr[i] === "-") {
      newStr = "-" + newStr;
      break;
    }
    newStr += xStr[i];
  }

  const res = Number(newStr);
  if (res < INT_MIN || res > INT_MAX) {
    return 0;
  }
  return res;
};

console.log(reverse(-123));
console.log(reverse(120));
console.log(reverse(10));
console.log(reverse(1534236469));
console.log(reverse(-1534236469));
