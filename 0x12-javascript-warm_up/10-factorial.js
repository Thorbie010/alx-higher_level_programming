#!/usr/bin/node
function computeFactorial(number){
    if (isNaN(number)){
        return 1;
    }
    else if (number <= 1){
        return 1;    
    }
    else {
        return number * computeFactorial(number - 1);
    }
}

const input = parseInt(process.argv[2]);
const output = computeFactorial(input);
console.log(output);