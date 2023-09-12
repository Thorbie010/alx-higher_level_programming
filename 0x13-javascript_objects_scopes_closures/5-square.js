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

  double () {
    this.width *= 2;
    for (let row = 0; row < this.height; row++) {
      console.log('x'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height * 2;
    this.height = temp;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Square;
