#!/usr/bin/node
const process = require('process');
const args = process.argv;
const n = args[2];

function factorial (n) {
  if (n === 0 || !n) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(n));
