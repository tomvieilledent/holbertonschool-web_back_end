export default function createInt8TypedArray(lenght, position, value) {
  if (position < 0 || position >= lenght) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(lenght);
  const view = new DataView(buffer);
  view.setInt8(position, value);
  return view;
}
