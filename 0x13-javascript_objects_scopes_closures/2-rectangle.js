#!/usr/bin/node
// class Rectangle that defines a rectangle, if w & h 0 or - create empty object
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
