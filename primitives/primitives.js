/**
 * PRIMITIVE DATA TYPES IN JAVASCRIPT
 * ==================================
 * 
 * In JavaScript, a primitive (primitive value, primitive data type) is data that is not an object and has no methods.
 * There are 7 primitive data types:
 * 1. string
 * 2. number
 * 3. bigint
 * 4. boolean
 * 5. undefined
 * 6. symbol
 * 7. null
 * 
 * All primitives are immutable, meaning they cannot be altered.
 */

// ==========================================
// 1. String
// ==========================================
console.log("--- 1. String ---");
// Basics:
let name = "John";
let singleQuote = 'Hello'; // Single quotes are also fine

// Template Literals (Backticks) - allow embedded expressions
let template = `Welcome, ${name}`;
console.log(template);

// Multiline Strings (using backticks)
let multi = `This is a
multiline string`;
console.log(multi);

// Advanced: Immutability
let str = "Hello";
// str[0] = "h"; // This does nothing (in strict mode, it might throw error)
console.log(str); // Output: "Hello"
// However, the variable can be reassigned
str = "World";
console.log(str); // Output: "World"

// ==========================================
// 2. Number
// ==========================================
console.log("\n--- 2. Number ---");
// Basics:
let age = 25;
let price = 19.99;

// Advanced: Special numeric values
let infinity = Infinity;
let negativeInfinity = -Infinity;
let notANumber = NaN; // Result of invalid math operation

console.log(1 / 0); // Infinity
console.log("text" / 2); // NaN

// Floating point precision issue (IEEE 754)
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3); // false

// range
console.log(Number.MAX_SAFE_INTEGER); // 2^53 - 1

// Binary, Octal, Hex representations
console.log(0b1010); // Binary (10)
console.log(0o12);   // Octal (10)
console.log(0xA);    // Hex (10)

// ==========================================
// 3. BigInt
// ==========================================
console.log("\n--- 3. BigInt ---");
// Created by appending 'n' to the end of an integer
// Used for numbers larger than Number.MAX_SAFE_INTEGER
// let bigNumber = 1234567890123456789012345678901234567890n; // Syntax depends on environment support
console.log(0n);     // BigInt (0)
let anotherBig = BigInt("1234567890123456789012345678901234567890");

console.log(anotherBig);
// Note: You cannot mix BigInt and other types in operations
// console.log(1n + 2); // TypeError

// ==========================================
// 4. Boolean
// ==========================================
console.log("\n--- 4. Boolean ---");
let isActive = true;
let isDeleted = false;

// Advanced: Truthy and Falsy values
// Falsy values: false, 0, -0, 0.0, 0n, "", null, undefined, NaN
if (0) {
    console.log("This won't run");
} else {
    console.log("0 is falsy");
}

// ==========================================
// 5. Undefined
// ==========================================
console.log("\n--- 5. Undefined ---");
// A variable that has not been assigned a value is of type undefined.
let x;
console.log(x); // undefined
console.log(typeof x); // "undefined"

// ==========================================
// 6. Null
// ==========================================
console.log("\n--- 6. Null ---");
// Represents the intentional absence of any object value.
let y = null;
console.log(y); // null

// Advanced: typeof null bug
console.log(typeof null); // "object" (This is a historical bug in JS)

// Difference between null and undefined
// undefined means a variable has been declared but has not yet been assigned a value
// null is an assignment value. It can be assigned to a variable as a representation of no value
console.log(null == undefined); // true
console.log(null === undefined); // false

// ==========================================
// 7. Symbol
// ==========================================
console.log("\n--- 7. Symbol ---");
// A "Symbol" represents a unique identifier.
let id1 = Symbol("id");
let id2 = Symbol("id");

console.log(id1 === id2); // false - Symbols are always unique, even with same description

// Use case: Hidden object properties
let user = {
    name: "John"
};
let id = Symbol("id");
user[id] = 12345;
console.log(user[id]); // 12345

// Symbols are ignored in for...in loops
for (let key in user) {
    console.log(key); // only "name"
}
