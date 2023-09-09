// Sample board data (you can replace this with actual data)
const boardData = [
    {
        thumbnail: "board1-thumbnail.jpg",
        title: "My Mind Map 1",
        creator: "John Doe",
        lastEdited: "Sept 15, 2023",
    },
    {
        thumbnail: "board2-thumbnail.jpg",
        title: "My Mind Map 2",
        creator: "Jane Smith",
        lastEdited: "Sept 16, 2023",
    },
    // Add more board data as needed
];

// Function to create a board card
function createBoardCard(board) {
    const boardContainer = document.getElementById("board-container");

    const boardCard = document.createElement("div");
    boardCard.classList.add("board-card");

    const thumbnail = document.createElement("img");
    thumbnail.src = board.thumbnail;
    thumbnail.alt = "Board Thumbnail";

    const title = document.createElement("h3");
    title.textContent = board.title;

    const info = document.createElement("p");
    info.textContent = `Created by ${board.creator} | Last Edited: ${board.lastEdited}`;

    boardCard.appendChild(thumbnail);
    boardCard.appendChild(title);
    boardCard.appendChild(info);

    // Add click event to board card to open/edit the board (implement this functionality)
    boardCard.addEventListener("click", () => {
        // Implement logic to open/edit the board
        alert(`Open/edit ${board.title}`);
    });

    boardContainer.appendChild(boardCard);
}

// Function to initialize board cards
function initializeBoardCards() {
    boardData.forEach((board) => {
        createBoardCard(board);
    });
}

// Load board cards when the page loads
window.addEventListener("load", () => {
    initializeBoardCards();
});

// Implement "Create New Board" button functionality here (e.g., open a new board creation form)
const createBoardButton = document.getElementById("create-board-button");
createBoardButton.addEventListener("click", () => {
    // Implement logic to create a new board
    alert("Create a new board");
});
