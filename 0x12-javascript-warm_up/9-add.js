#!/usr/bin/node
const process = require('process');
const args = process.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);
let sum = 0;

function add (a, b) {
  sum = a + b;
  console.log(sum);
}
add(a,b);
