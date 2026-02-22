/**
 * NON-PRIMITIVE DATA TYPES IN JAVASCRIPT
 * ======================================
 * 
 * Non-primitive types are objects. They are mutable and stored by reference.
 * Main types:
 * 1. Object
 * 2. Array
 */

// ==========================================
// 1. Objects
// ==========================================
console.log("--- 1. Objects ---");
// Creation
const user = {
    name: "John",
    age: 30,
    isAdmin: true,
    // Methods
    greet: function () {
        console.log(`Hello, I am ${this.name}`);
    }
};

// Accessing
console.log(user.name); // Dot notation
console.log(user["age"]); // Bracket notation

// Modifying
user.age = 31;
user.city = "New York"; // Adding new property
delete user.isAdmin;    // Deleting property

// Looping over Objects
console.log("Looping Object:");
for (let key in user) {
    console.log(`${key}: ${user[key]}`);
}

// ==========================================
// 2. Arrays
// ==========================================
console.log("\n--- 2. Arrays ---");
// Creation
const numbers = [1, 2, 3, 4, 5];
const mixed = [1, "two", { id: 3 }];

// Accessing
console.log(numbers[0]); // 1
console.log(numbers.length); // 5

// Looping Arrays
console.log("Looping Array (for...of):");
for (const num of numbers) {
    console.log(num);
}

// Standard loops
console.log("Looping Array (Standard for):");
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// ==========================================
// 3. Array High-Order Methods
// ==========================================
console.log("\n--- 3. Array Methods (Functional) ---");

const items = [
    { name: 'Bike', price: 100 },
    { name: 'TV', price: 200 },
    { name: 'Album', price: 10 },
    { name: 'Book', price: 5 },
    { name: 'Phone', price: 500 },
    { name: 'Computer', price: 1000 },
];

console.log("Original Items:", items);

// 1. FILTER: Returns a new array with all elements that pass the test
// Get items cheaper than 100
const cheapItems = items.filter((item) => {
    return item.price < 100;
});
console.log("Filtered (Cheap Items):", cheapItems);

// 2. MAP: Returns a new array by applying a function to every element
// Get just the names of items
const itemNames = items.map((item) => {
    return item.name;
});
console.log("Mapped (Names):", itemNames);

// 3. FIND: Returns the value of the FIRST element that passes the test
// Find the item with name 'Book'
const foundItem = items.find((item) => {
    return item.name === 'Book';
});
console.log("Found Item 'Book':", foundItem);

// 4. REDUCE: Reduces the array to a single value
// Calculate total price of all items
// Syntax: array.reduce((accumulator, currentItem) => { ... }, initialValue)
const total = items.reduce((currentTotal, item) => {
    return item.price + currentTotal;
}, 0);
console.log("Total Price (Reduce):", total);

// 5. forEach: Executes a provided function once for each array element (No return value)
console.log("forEach Output:");
items.forEach((item) => {
    console.log(`- ${item.name}: $${item.price}`);
});
