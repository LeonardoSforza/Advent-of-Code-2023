const fs = require('fs');

const filePath = './testData.txt';

const mapOfSeeds = {};

// Function to add or update a value in the map under a specific key
function addToMap(key, value) {
  if (!mapOfSeeds[key]) {
    // If the key doesn't exist, initialize it with an empty array
    mapOfSeeds[key] = [];
  }

  const index = mapOfSeeds[key].indexOf(value);
  if (index === -1) {
    // If the value is not already in the array, add it
    mapOfSeeds[key].push(value);
  } else {
    // If the value is already in the array, update it (replace)
    mapOfSeeds[key][index] = value;
  }
}


fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }

  // Split the file content into an array of lines
  const lines = data.split('\n');

  // Remove empty lines (if any)
  const nonEmptyLines = lines.filter(line => line.trim() !== '');

  // Example usage
    addToMap('someKey', '[value1]');
    addToMap('someKey', '[value2]');
    addToMap('anotherKey', '[value3]');
    console.log(mapOfSeeds);
    addToMap('someKey', '[value1]'); // This will update 'value1'
    console.log(mapOfSeeds);
});
