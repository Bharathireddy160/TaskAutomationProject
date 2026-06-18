import customtkinter as ctk
from tkinter import messagebox

from scraper.fetcher import get_website_title
from scraper.saver import save_title


# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class WebScraperApp:

    def __init__(self):

        self.root = ctk.CTk()
        self.root.title("Web Scraper Automation")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.create_ui()

        self.root.mainloop()

    def create_ui(self):

        # Title
        self.title_label = ctk.CTkLabel(
            self.root,
            text="🌐 WEBSITE SCRAPER AUTOMATION",
            font=("Arial", 28, "bold")
        )
        self.title_label.pack(pady=30)

        # Main frame
        self.frame = ctk.CTkFrame(
            self.root,
            width=700,
            height=350,
            corner_radius=20
        )
        self.frame.pack(pady=10)

        # URL label
        self.url_label = ctk.CTkLabel(
            self.frame,
            text="Enter Website URL",
            font=("Arial", 18)
        )
        self.url_label.pack(pady=(30, 10))

        # URL entry
        self.url_entry = ctk.CTkEntry(
            self.frame,
            width=500,
            height=40,
            placeholder_text="https://example.com",
            font=("Arial", 14)
        )
        self.url_entry.pack(pady=10)

        # Button
        self.scrape_button = ctk.CTkButton(
            self.frame,
            text="Extract Title",
            width=200,
            height=45,
            font=("Arial", 16, "bold"),
            command=self.scrape_website
        )
        self.scrape_button.pack(pady=25)

        # Result box
        self.result_label = ctk.CTkLabel(
            self.frame,
            text="Waiting for input...",
            font=("Arial", 16),
            wraplength=600
        )
        self.result_label.pack(pady=15)

        # Status box
        self.status_label = ctk.CTkLabel(
            self.frame,
            text="",
            font=("Arial", 14)
        )
        self.status_label.pack(pady=10)

    def scrape_website(self):

        url = self.url_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a valid URL")
            return

        self.result_label.configure(text="Fetching website...")

        title = get_website_title(url)

        if title:

            save_title(title)

            self.result_label.configure(
                text=f"Website Title Found:\n\n{title}"
            )

            self.status_label.configure(
                text="✅ Title saved successfully in output folder"
            )

        else:
            messagebox.showerror(
                "Error",
                "Unable to fetch website title"
            )


if __name__ == "__main__":
    WebScraperApp()
    