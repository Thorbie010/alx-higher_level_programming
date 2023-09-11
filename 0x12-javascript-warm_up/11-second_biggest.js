#!/usr/bin/node
if ((process.argv.length === 3) || (process.argv.length <= 2)) {
  console.log('0');
} else if (process.argv.length > 3) {
  const nums = process.argv.slice(2).map(Number);
  const uniquesortednumbers = [...new Set(nums)].sort((a, b) => b - a);
  if (uniquesortednumbers.lenght < 2) {
    console.log('0');
  } else {
    console.log(uniquesortednumbers[1]);
  }
}
