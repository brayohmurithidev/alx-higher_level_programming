#!/usr/bin/node
const args = process.argv.slice(2);
const arg1 = Number(args[0]);
const arg2 = Number(args[1]);
function add (a, b) {
  console.log(a + b);
}
add(arg1, arg2);
