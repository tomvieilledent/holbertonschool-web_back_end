const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};
      let output = `Number of students: ${students.length}\n`;

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (field) {
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
        }
      });

      // Print to console as required
      console.log(`Number of students: ${students.length}`);
      Object.entries(fields).forEach(([field, list]) => {
        const line = `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
        console.log(line);
        output += `${line}\n`;
      });

      resolve(output);
    });
  });
}

module.exports = countStudents;
