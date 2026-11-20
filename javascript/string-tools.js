'use strict';
function slugify(value) {
  if (typeof value !== 'string') throw new TypeError('value must be a string');
  return value.normalize('NFKD').toLowerCase().replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}
function countWords(value) {
  if (typeof value !== 'string') throw new TypeError('value must be a string');
  const text = value.trim();
  return text ? text.split(/\s+/).length : 0;
}
module.exports = { slugify, countWords };
