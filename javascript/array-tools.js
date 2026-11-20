"use strict";

/** Return unique values while preserving their first occurrence. */
function unique(items) {
  if (!Array.isArray(items)) throw new TypeError("items must be an array");
  return [...new Set(items)];
}

/** Group values by a key-producing function. */
function groupBy(items, keyFn) {
  if (!Array.isArray(items) || typeof keyFn !== "function") {
    throw new TypeError("expected an array and a key function");
  }
  return items.reduce((groups, item) => {
    const key = keyFn(item);
    (groups[key] ??= []).push(item);
    return groups;
  }, {});
}

if (require.main === module) {
  console.log(unique([1, 1, 2, 3]));
  console.log(groupBy(["ant", "apple", "bee"], x => x[0]));
}

module.exports = { unique, groupBy };
