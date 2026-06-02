import tkinter as tk
from tkinter import filedialog, messagebox
import imageio.v3 as iio


def select_files():
    # Opens a file explorer dialog to select multiple PNG images
    file_paths = filedialog.askopenfilenames(
        title="Select Images for GIF",
        filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")]
    )

    # If the user selected files, update the listbox and save the paths
    if file_paths:
        selected_files_list.set(file_paths)
        listbox.delete(0, tk.END)
        for path in file_paths:
            listbox.insert(tk.END, path.split('/')[-1])  # Shows just the filename in the UI


def make_gif():
    # Retrieve the full file paths from our list
    files = selected_files_list.get()

    if not files:
        messagebox.showwarning("Warning", "Please select some images first!")
        return

    # Ask where to save the finished GIF
    save_path = filedialog.asksaveasfilename(
        title="Save GIF As",
        defaultextension=".gif",
        filetypes=[("GIF Files", "*.gif")]
    )

    if not save_path:
        return  # User cancelled saving

    try:
        images = []
        for filename in files:
            images.append(iio.imread(filename))

        # Create the GIF using your exact settings
        iio.imwrite(save_path, images, duration=500, loop=0)
        messagebox.showinfo("Success!", f"GIF successfully saved to:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")


# --- GUI Window Setup ---
root = tk.Tk()
root.title("Team GIF Maker")
root.geometry("400x350")

# Variable to store the full file paths hidden from plain view
selected_files_list = tk.Variable()

# UI Layout
label = tk.Label(root, text="Convert PNGs to an Animated GIF", font=("Arial", 12, "bold"))
label.pack(pady=10)

btn_select = tk.Button(root, text="1. Upload PNG Files", command=select_files, bg="#4CAF50", fg="white", padx=10,
                       pady=5)
btn_select.pack(pady=5)

# A small window box to display the files you uploaded
listbox = tk.Listbox(root, width=45, height=8)
listbox.pack(pady=10)

btn_convert = tk.Button(root, text="2. Create & Save GIF", command=make_gif, bg="#008CBA", fg="white", padx=10, pady=5)
btn_convert.pack(pady=5)

root.mainloop()