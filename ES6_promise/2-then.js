export default function handleResponseFromAPI(promise) {
  return promise === true
    ? Promise.resolve({ status: 200, bodu: 'success' }, console.log("Got a response from the API"))
    : Promise.reject(new Error()), console.log("Got a response from the API");
}
