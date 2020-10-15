let input = document.getElementById("input");
let result = document.getElementById("result");
let button = document.getElementById("button");

function getfigures() {
  if (!input.checkValidity()) {
    result.innerHTML = "invalid input";
    return;
  }
  let xhttp = new XMLHttpRequest;
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      result.innerHTML = JSON.parse(this.responseText)["figs"];
    }
  };
  xhttp.open("POST", "/figures", true);
  xhttp.setRequestHeader("Content-Type", "application/json");
  xhttp.send(JSON.stringify({"number": input.value}));
}

button.addEventListener("click", getfigures);
