export default class HolbertonCourse {
  constructor(name, lenght, students) {
    if (typeof name === 'string') {
      this._name = name;
    }
    if (typeof lenght === 'number') {
      this._lenght = lenght;
    }
    if (
      Array.isArray(students)
      && students.every((student) => typeof student === 'string')
    ) {
      this._students = students;
    }
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }

    this._name = value;
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }

    this._lenght = value;
  }

  get students() {
    return this._students;
  }

  set students(value) {
    if (
      !Array.isArray(value)
      || !value.every((student) => typeof student === 'string')
    ) {
      throw new TypeError('Students must be an array of strings');
    }

    this._students = value;
  }
}
