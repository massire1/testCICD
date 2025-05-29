function getMessage() {
  fetch("http://localhost:5001/api/hello")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("message").innerText = data.message;
    });
}
