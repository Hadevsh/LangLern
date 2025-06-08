document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.flashcard').forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('flipped');
        });
    });

    document.getElementById("submit").addEventListener("click", async event => {
        event.preventDefault();
        const word = document.getElementById("word-input").value.trim();
        const from_code = "en";
        const to_code = "nl";

        const res = await fetch("/translate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ word, from_code, to_code })
        });

        const data = await res.json();
        const resultDiv = document.getElementById("translated");
        if (res.ok) {
            resultDiv.innerHTML = `${data.translation}`;
        } else {
            resultDiv.innerHTML = `Error: ${data.error}`;
        }
    });
});

