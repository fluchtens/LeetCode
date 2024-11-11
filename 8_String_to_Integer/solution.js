/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {
  const INT_MIN = Math.pow(-2, 31);
  const INT_MAX = Math.pow(2, 31) - 1;

  const nb = parseInt(s);
  if (isNaN(nb)) {
    return 0;
  } else if (nb < INT_MIN) {
    return INT_MIN;
  } else if (nb > INT_MAX) {
    return INT_MAX;
  }
  return nb;
};
