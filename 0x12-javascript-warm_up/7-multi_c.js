#!/usr/bin/node
const times = parseInt(process.argv[2]);

if (!isNaN(times)) {
  let output = '';
  for (let i = 0; i < times; i++) {
    output += 'C is fun\n';
  }
  console.log(output);
} else {
  console.log('Missing number of occurences');
}
