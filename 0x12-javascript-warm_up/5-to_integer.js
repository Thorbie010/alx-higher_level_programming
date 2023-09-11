#!/usr/bin/node
const argc = process.argv[2];
const intArgc = parseInt(argc, 10);
if (!isNaN(intArgc)) {
  console.log('My number: ' + intArgc);
} else { console.log('Not a number'); }
