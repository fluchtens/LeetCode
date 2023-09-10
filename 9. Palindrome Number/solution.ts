function isPalindrome(x: number): boolean {
  if (!x) {
    return (true);
  }

  const str: string = x.toString();
  const strLen: number = str.length;

  let j: number = strLen - 1;
  for (let i: number = 0; i < strLen - 1; i++) {
    if (str[i] !== str[j]) {
      return (false);
    }
    j--;
  }

  return (true);
};

console.log(isPalindrome(0));
console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));
console.log(isPalindrome(1000021));
