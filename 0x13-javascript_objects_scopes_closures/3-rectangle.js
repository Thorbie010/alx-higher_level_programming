#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      console.log('');
    } else {
      for (let row = 0; row < this.height; row++) {
        console.log('x'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
