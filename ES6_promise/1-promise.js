export default function getFullResponseFromAPI(success) {
  return success === true
    ? Promise.resolve({ status: 200, body: 'Succes' })
    : Promise.reject(new Error('The fake API is not working currently'));
}
