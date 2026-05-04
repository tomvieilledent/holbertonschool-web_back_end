export default function cleanSet(set, startString) {
  const selectedSet = [...set].filter((value) => value.startsWith(startString));
  const list = selectedSet.map((value) => value.slice(startString.length)).join('-');
  return list;
}
