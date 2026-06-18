import tkinter as tk
from tkinter import messagebox

from scraper.fetcher import get_website_title
from scraper.saver import save_title


def scrape_website():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    title = get_website_title(url)

    if title:
        save_title(title)

        result_label.config(text=f"Website Title:\n{title}")
        status_label.config(text="Saved successfully in output folder")

    else:
        messagebox.showerror("Error", "Could not fetch website title")


# Main window
root = tk.Tk()
root.title("Website Title Scraper")
root.geometry("600x400")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="WEBSITE SCRAPER AUTOMATION",
    font=("Arial", 18, "bold")
)
heading.pack(pady=20)

# URL input
url_label = tk.Label(root, text="Enter Website URL:", font=("Arial", 12))
url_label.pack()

url_entry = tk.Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=10)

# Button
scrape_button = tk.Button(
    root,
    text="SCRAPE WEBSITE",
    font=("Arial", 12),
    command=scrape_website,
    width=20
)
scrape_button.pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 13))
result_label.pack(pady=20)

# Status
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()