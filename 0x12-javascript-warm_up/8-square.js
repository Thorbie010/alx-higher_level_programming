#!/usr/bin/node
const times = parseInt(process.argv[2]);

if (!isNaN(times)) {
  for (let i = 0; i < times; i++) {
    let output = '';
    for (let x = 0; x < times; x++) {
      output += 'X';
    }
    console.log(output);
  }
} else {
  console.log('Missing size');
}
