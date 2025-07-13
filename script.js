document.addEventListener("DOMContentLoaded", () => {
    const switcher = document.getElementById("themeSwitcher");
    const body = document.body;

    // Load saved theme
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark-mode");
        switcher.checked = true;
    }

    switcher.addEventListener("change", () => {
        body.classList.toggle("dark-mode");
        localStorage.setItem("theme", body.classList.contains("dark-mode") ? "dark" : "light");
    });
});
