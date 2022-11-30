#!/usr/bin/node

const args = process.argv.slice(2);

const strToNum = Number(args[0]);
if (isNaN(strToNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < strToNum; i++) {
    console.log('X'.repeat(args));
  }
}
