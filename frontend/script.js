const form = document.getElementById("generatorForm");
const loading = document.getElementById("loading");
const status = document.getElementById("status");
const button = form.querySelector("button");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    status.innerHTML = "";

    button.disabled = true;
    loading.classList.remove("hidden");

    const theme = document.getElementById("theme").value;
    const age = parseInt(document.getElementById("age").value);
    const pages = parseInt(document.getElementById("pages").value);

    try {

        const response = await fetch("http://127.0.0.1:8000/api/v1/colorbook", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                theme,
                age,
                pages
            })
        });

        if (!response.ok) {
            throw new Error("Generation failed.");
        }

        const blob = await response.blob();

        const url = window.URL.createObjectURL(blob);

        const a = document.createElement("a");
        a.href = url;
        a.download = "coloring_book.pdf";

        document.body.appendChild(a);
        a.click();

        a.remove();

        window.URL.revokeObjectURL(url);

        status.style.color = "green";
        status.innerHTML = "✅ Coloring book downloaded successfully!";

    } catch (error) {

        status.style.color = "red";
        status.innerHTML = error.message;

    } finally {

        loading.classList.add("hidden");
        button.disabled = false;

    }
});