import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from encryption import caesar
from encryption import vigenere
from encryption import playfair

from steganography import lsb


class StegoCryptApp:

    def __init__(self, root):
        self.root = root

        self.root.title("StegoCrypt - Encryption & Steganography")
        self.root.geometry("850x650")
        self.root.resizable(False, False)

        self.selected_image = None

        self.create_interface()

    def create_interface(self):

        title = tk.Label(
            self.root,
            text="StegoCrypt",
            font=("Arial", 26, "bold")
        )

        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self.root,
            text="Encryption & LSB Image Steganography",
            font=("Arial", 12)
        )

        subtitle.pack(pady=(0, 20))

        notebook = ttk.Notebook(self.root)

        notebook.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=10
        )

        self.create_encrypt_tab(notebook)
        self.create_extract_tab(notebook)

    def create_encrypt_tab(self, notebook):

        frame = ttk.Frame(notebook)

        notebook.add(
            frame,
            text="Encrypt & Hide"
        )

        tk.Label(
            frame,
            text="Encryption Algorithm"
        ).pack(pady=(20, 5))

        self.algorithm = ttk.Combobox(
            frame,
            values=[
                "Caesar Cipher",
                "Vigenere Cipher",
                "Playfair Cipher"
            ],
            state="readonly",
            width=30
        )

        self.algorithm.current(0)
        self.algorithm.pack()

        tk.Label(
            frame,
            text="Encryption Key"
        ).pack(pady=(15, 5))

        self.key_entry = tk.Entry(
            frame,
            width=35,
            show="*"
        )

        self.key_entry.pack()

        tk.Label(
            frame,
            text="Message"
        ).pack(pady=(15, 5))

        self.message_text = tk.Text(
            frame,
            height=8,
            width=70
        )

        self.message_text.pack()

        tk.Button(
            frame,
            text="Select Cover Image",
            command=self.select_image
        ).pack(pady=15)

        self.image_label = tk.Label(
            frame,
            text="No image selected"
        )

        self.image_label.pack()

        tk.Button(
            frame,
            text="Encrypt & Hide Message",
            command=self.encrypt_and_hide,
            width=30
        ).pack(pady=20)

    def create_extract_tab(self, notebook):

        frame = ttk.Frame(notebook)

        notebook.add(
            frame,
            text="Extract & Decrypt"
        )

        tk.Label(
            frame,
            text="Stego Image"
        ).pack(pady=(25, 5))

        tk.Button(
            frame,
            text="Select Stego Image",
            command=self.select_stego_image
        ).pack()

        self.stego_image_label = tk.Label(
            frame,
            text="No image selected"
        )

        self.stego_image_label.pack(pady=10)

        tk.Label(
            frame,
            text="Encryption Algorithm"
        ).pack(pady=(15, 5))

        self.decrypt_algorithm = ttk.Combobox(
            frame,
            values=[
                "Caesar Cipher",
                "Vigenere Cipher",
                "Playfair Cipher"
            ],
            state="readonly",
            width=30
        )

        self.decrypt_algorithm.current(0)
        self.decrypt_algorithm.pack()

        tk.Label(
            frame,
            text="Decryption Key"
        ).pack(pady=(15, 5))

        self.decrypt_key_entry = tk.Entry(
            frame,
            width=35,
            show="*"
        )

        self.decrypt_key_entry.pack()

        tk.Button(
            frame,
            text="Extract & Decrypt",
            command=self.extract_and_decrypt,
            width=30
        ).pack(pady=25)

        tk.Label(
            frame,
            text="Recovered Message"
        ).pack(pady=(10, 5))

        self.result_text = tk.Text(
            frame,
            height=8,
            width=70
        )

        self.result_text.pack()

    def select_image(self):

        path = filedialog.askopenfilename(
            title="Select Cover Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
                ("All Files", "*.*")
            ]
        )

        if path:
            self.selected_image = path

            self.image_label.config(
                text=path
            )

    def select_stego_image(self):

        path = filedialog.askopenfilename(
            title="Select Stego Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
                ("All Files", "*.*")
            ]
        )

        if path:
            self.selected_stego_image = path

            self.stego_image_label.config(
                text=path
            )

    def encrypt_message(self, message, algorithm, key):

        if algorithm == "Caesar Cipher":

            try:
                shift = int(key)
            except ValueError:
                raise ValueError(
                    "Caesar Cipher key must be a number."
                )

            return caesar.encrypt(
                message,
                shift
            )

        if algorithm == "Vigenere Cipher":

            return vigenere.encrypt(
                message,
                key
            )

        if algorithm == "Playfair Cipher":

            return playfair.encrypt(
                message,
                key
            )

        raise ValueError(
            "Invalid encryption algorithm."
        )

    def decrypt_message(self, message, algorithm, key):

        if algorithm == "Caesar Cipher":

            try:
                shift = int(key)
            except ValueError:
                raise ValueError(
                    "Caesar Cipher key must be a number."
                )

            return caesar.decrypt(
                message,
                shift
            )

        if algorithm == "Vigenere Cipher":

            return vigenere.decrypt(
                message,
                key
            )

        if algorithm == "Playfair Cipher":

            return playfair.decrypt(
                message,
                key
            )

        raise ValueError(
            "Invalid decryption algorithm."
        )

    def encrypt_and_hide(self):

        try:

            if not self.selected_image:
                raise ValueError(
                    "Please select a cover image."
                )

            message = self.message_text.get(
                "1.0",
                tk.END
            ).strip()

            if not message:
                raise ValueError(
                    "Please enter a message."
                )

            key = self.key_entry.get().strip()

            if not key:
                raise ValueError(
                    "Please enter an encryption key."
                )

            algorithm = self.algorithm.get()

            encrypted_message = self.encrypt_message(
                message,
                algorithm,
                key
            )

            output_path = filedialog.asksaveasfilename(
                title="Save Stego Image",
                defaultextension=".png",
                filetypes=[
                    ("PNG Image", "*.png")
                ]
            )

            if not output_path:
                return

            lsb.hide_message(
                self.selected_image,
                output_path,
                encrypted_message
            )

            messagebox.showinfo(
                "Success",
                "Message encrypted and hidden successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def extract_and_decrypt(self):

        try:

            if not hasattr(
                self,
                "selected_stego_image"
            ):
                raise ValueError(
                    "Please select a stego image."
                )

            key = self.decrypt_key_entry.get().strip()

            if not key:
                raise ValueError(
                    "Please enter the decryption key."
                )

            algorithm = self.decrypt_algorithm.get()

            encrypted_message = lsb.extract_message(
                self.selected_stego_image
            )

            decrypted_message = self.decrypt_message(
                encrypted_message,
                algorithm,
                key
            )

            self.result_text.delete(
                "1.0",
                tk.END
            )

            self.result_text.insert(
                tk.END,
                decrypted_message
            )

            messagebox.showinfo(
                "Success",
                "Message extracted and decrypted successfully."
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )


def main():

    root = tk.Tk()

    app = StegoCryptApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
