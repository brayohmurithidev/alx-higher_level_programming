#!/usr/bin/node
const args = process.argv.slice(2);
const strToNum = Number(args[0]);
const arg1 = isNaN(strToNum) ? 1 : strToNum;

function factorial (a) {
  if (a === 0) return 1;
  return a * factorial(a - 1);
}

console.log(factorial(arg1));
