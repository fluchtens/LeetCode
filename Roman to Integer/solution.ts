function romanToInt(str: string): number {
  const config: { [symbol: string]: number } = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  };

  let result: number = 0;

  for (let i: number = 0; i < str.length; i++) {
    const currentRomanValue: number = config[str[i]];
    const nextRomanValue: number = config[str[i + 1]];

    if (nextRomanValue && currentRomanValue < nextRomanValue) {
      result -= currentRomanValue;
    } else {
      result += currentRomanValue;
    }
  }

  return (result);
};

console.log(romanToInt("III"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("MCMXCIV"));
