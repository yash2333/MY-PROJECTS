'use strict';
function unique(items) {
  if (!Array.isArray(items)) throw new TypeError('items must be an array');
  return [...new Set(items)];
}
function groupBy(items, keyFn) {
  if (!Array.isArray(items) || typeof keyFn !== 'function') throw new TypeError('expected array and key function');
  return items.reduce((groups, item) => {
    const key = keyFn(item);
    (groups[key] ??= []).push(item);
    return groups;
  }, {});
}
module.exports = { unique, groupBy };
