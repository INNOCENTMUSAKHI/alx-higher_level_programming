#!/usr/bin/node
const process = require('process');
const args = process.argv;
const array = [];
if (!args[2] || args.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    array.push(args[i]);
  }
  array.sort(function (a, b) { return a - b; });
  console.log(array.slice(-2)[0]);
}
