import * as fs from "fs";

const filePath = "input_day1.txt";
const inputString = fs.readFileSync(filePath, "utf8").trim();
const lines = inputString.split("\n");

var leftArray: number[] = [];
var rightArray: number[] = [];

lines.forEach(line => {
    const [left, right] = line.trim().split(/\s+/).map(Number);
    leftArray.push(left);
    rightArray.push(right);
});

leftArray = leftArray.sort((a, b) => a - b);
rightArray = rightArray.sort((a, b) => a - b);

if (leftArray.length !== rightArray.length) {
    throw new Error("Mismatched array lengths!");
}

const distance = leftArray
    .map((left, idx) => Math.abs(left - rightArray[idx]))
    .reduce((sum, val) => sum + val, 0);

console.log(distance);

const counts = new Map<number, number>();
rightArray.forEach(right => {
    const count = counts.get(right) || 0;
    counts.set(right, count + 1);
});

const similarity = leftArray.reduce((sum, left) => {
    const count = counts.get(left) || 0;
    return sum + left * count;
}, 0);

console.log(similarity);
