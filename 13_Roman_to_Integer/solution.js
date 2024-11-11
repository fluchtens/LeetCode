/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const map = new Map();
  map.set("I", 1);
  map.set("V", 5);
  map.set("X", 10);
  map.set("L", 50);
  map.set("C", 100);
  map.set("D", 500);
  map.set("M", 1000);

  let res = 0;
  for (let i = 0; i < s.length; i++) {
    const current = map.get(s[i]);
    const next = map.get(s[i + 1]);

    if (next && current < next) {
      res -= current;
    } else {
      res += current;
    }
  }
  return res;
};
