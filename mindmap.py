import tkinter as tk
from tkhtmlview import HTMLLabel
import os

class MindMapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mind Map Application")

        # Create top navigation bar
        self.top_nav = tk.Frame(root, bg="blue", height=50)
        self.top_nav.pack(fill=tk.X)

        # Add user profile icon/avatar on the right
        self.profile_icon = tk.Label(self.top_nav, text="User Avatar", bg="blue", fg="white", padx=10)
        self.profile_icon.pack(side=tk.RIGHT)

        # Create side navigation panel
        self.side_nav = tk.Frame(root, bg="lightgray", width=200)
        self.side_nav.pack(fill=tk.Y, side=tk.LEFT)

        # Add navigation links
        self.home_button = tk.Button(self.side_nav, text="Home", command=self.show_home)
        self.home_button.pack(pady=10)

        self.profile_button = tk.Button(self.side_nav, text="Profile", command=self.show_profile)
        self.profile_button.pack(pady=10)

        self.boards_button = tk.Button(self.side_nav, text="Mind Map Boards", command=self.show_boards)
        self.boards_button.pack(pady=10)

        self.settings_button = tk.Button(self.side_nav, text="Settings", command=self.show_settings)
        self.settings_button.pack(pady=10)

        # Create main content area using tkhtmlview
        self.main_content = HTMLLabel(self.root, bg="white")
        self.main_content.pack(fill=tk.BOTH, expand=True)

        # Initialize the content as the home page
        self.show_home()

    def load_html_file(self, filename):
        # Load and return the content of an HTML file
        html_file = os.path.join("web_content", filename)
        with open(html_file, "r") as file:
            html_content = file.read()
        return html_content

    def show_home(self):
        # Display the home page using HTML content from "home.html"
        html_content = self.load_html_file("home.html")
        self.main_content.set_html(html_content)

    def show_profile(self):
        # Display the profile page using HTML content from "profile.html"
        html_content = self.load_html_file("profile.html")
        self.main_content.set_html(html_content)

    def show_boards(self):
        # Display the Mind Map Boards page using HTML content from "boards.html"
        html_content = self.load_html_file("boards.html")
        self.main_content.set_html(html_content)

    def show_settings(self):
        # Display the Settings page using HTML content from "settings.html"
        html_content = self.load_html_file("settings.html")
        self.main_content.set_html(html_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = MindMapApp(root)
    root.mainloop()
