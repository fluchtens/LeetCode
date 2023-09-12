function lengthOfLongestSubstring(str: string): number {
  let result: string[] = [];

  const isDuplicateChar = (char: string, str: string) => {
    if (str) {
      for (let i: number = 0; i < str.length; i++) {
        if (char === str[i]) {
          return (true);
        }
      }
    }
    return (false);
  }

  let tabIndex: number = 0;
  let firstChar: boolean = true;

  for (let i: number = 0; i < str.length; i++) {
    if (isDuplicateChar(str[i], result[tabIndex])) {
      tabIndex++;
      firstChar = true;
    }
    if (firstChar) {
      result[tabIndex] = "";
      firstChar = false;
    }
    result[tabIndex] += str[i];
  }

  for (let i: number = 0; i < result.length; i++) {
    const currenLength: number = result[i].length;
    let biggestLength: number = currenLength;

    if (result[i + 1]) {
      const nextLength: number = result[i + 1].length;
      if (nextLength > biggestLength) {
        biggestLength = nextLength;
      }
    }
  
    return (biggestLength);
  }

  return (0);
};

console.log(lengthOfLongestSubstring("abcabcbb"));
console.log(lengthOfLongestSubstring("bbbbb"));
console.log(lengthOfLongestSubstring("pwwkew"));
console.log(lengthOfLongestSubstring("dvdf"));
