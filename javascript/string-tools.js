"use strict";

/** Convert a phrase to a URL-friendly slug. */
function slugify(value) {
  if (typeof value !== "string") throw new TypeError("value must be a string");
  return value.normalize("NFKD").toLowerCase()
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

/** Count words separated by whitespace. */
function countWords(value) {
  if (typeof value !== "string") throw new TypeError("value must be a string");
  const trimmed = value.trim();
  return trimmed ? trimmed.split(/\s+/).length : 0;
}

if (require.main === module) {
  console.log(slugify("B.Tech CSE Portfolio"));
  console.log(countWords("Build useful things"));
}

module.exports = { slugify, countWords };
