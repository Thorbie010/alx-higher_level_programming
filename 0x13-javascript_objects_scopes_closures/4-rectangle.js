#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
        console.log('x'.repeat(this.width));
      }
    }


  double () {
    this.width *= 2;
    this.height *= 2;
  }
  

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

module.exports = Rectangle;
