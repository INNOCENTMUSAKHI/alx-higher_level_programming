#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (!args[2] || isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('X'.repeat(args[2]));
  }
}
