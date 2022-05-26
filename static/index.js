document.getElementById("calc-form").addEventListener("submit", (event) => {
    event.preventDefault();
    expression = event.target.elements.expression.value;
    fetch("/calc", {
        body: expression,
        method: 'POST'
    })
        .then(response => response.text())
        .then(answer => {
            document.getElementById('ans-txt').innerHTML = answer;
        });

});