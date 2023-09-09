document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll("nav a");
    const toggleButton = document.getElementById("toggle-panel-button");
    const nav = document.querySelector("nav");
    const contentDiv = document.getElementById("content");

    // Function to load content into the main content area
    function loadContent(url) {
        fetch(url)
            .then((response) => response.text())
            .then((data) => {
                contentDiv.innerHTML = data;
            })
            .catch((error) => {
                console.error("Error loading content: ", error);
            });
    }

    // Function to close the navigation
    function closeNavigation() {
        nav.style.top = "-100%"; // Move the navigation off-screen
        contentDiv.classList.remove("shifted"); // Reset content position
    }

    // Close the navigation when a navigation link is clicked
    navLinks.forEach((link) => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const href = link.getAttribute("href");
            loadContent(`web_content/${href}`);
            closeNavigation();
        });
    });

    // Toggle the navigation when the toggle button is clicked
    toggleButton.addEventListener("click", () => {
        if (nav.style.top === "-100%") {
            nav.style.top = "0"; // Move the navigation onto the screen
            contentDiv.classList.add("shifted"); // Shift content when navigation opens
        } else {
            closeNavigation(); // Close the navigation if already open
        }
    });

    // Load the default content (home.html) when the page loads
    loadContent("web_content/home.html");
});
