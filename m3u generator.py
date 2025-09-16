import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def generate_m3u_file():
    game_name = game_name_entry.get().strip()
    try:
        num_discs = int(disc_count_entry.get())
        if num_discs < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number of discs (1 or more).")
        return

    if not game_name:
        messagebox.showerror("Missing Game Name", "Please enter the base name of the CHD files.")
        return

    # Ask where to save the file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".m3u",
        initialfile=f"{game_name}.m3u",
        filetypes=[("M3U Playlist", "*.m3u")]
    )
    if not file_path:
        return  # User cancelled

    # Generate the list of CHD filenames
    lines = [f"{game_name} (Disc {i}).chd" for i in range(1, num_discs + 1)]

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        messagebox.showinfo("Success", f"M3U file saved:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write file:\n{e}")


# Set up the GUI
root = tk.Tk()
root.title("M3U Generator for CHD Games")

# Game Name
tk.Label(root, text="Game Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
game_name_entry = tk.Entry(root, width=40)
game_name_entry.grid(row=0, column=1, padx=10, pady=5)

# Number of Discs
tk.Label(root, text="Number of Discs:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
disc_count_entry = tk.Entry(root, width=5)
disc_count_entry.insert(0, "2")
disc_count_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Generate Button
generate_button = tk.Button(root, text="Generate M3U", command=generate_m3u_file)
generate_button.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()
