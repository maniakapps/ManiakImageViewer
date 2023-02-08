from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.images = []
        self.current_image = 0

    def create_widgets(self):
        self.open_button = Button(self)
        self.open_button["text"] = "Open"
        self.open_button["command"] = self.load_images
        self.open_button.pack()

        self.previous_button = Button(self)
        self.previous_button["text"] = "Previous"
        self.previous_button["command"] = self.previous_image
        self.previous_button.pack()

        self.next_button = Button(self)
        self.next_button["text"] = "Next"
        self.next_button["command"] = self.next_image
        self.next_button.pack()

        self.quit = Button(self, text="QUIT", fg="red",
                           command=root.destroy)
        self.quit.pack()

    def load_images(self):
        files = filedialog.askopenfilenames(title="Select Images",
                                            filetypes=(("Images", "*.jpg;*.jpeg;*.png;*.gif"), ("All Files", "*.*")))
        for file in files:
            image = Image.open(file)
            width, height = image.size
            if width > 1080:
                height = int(height * 1080 / width)
                width = 1080
            if height > 720:
                width = int(width * 720 / height)
                height = 720
            image = image.resize((width, height), Image.ANTIALIAS)
            self.images.append(ImageTk.PhotoImage(image))
        self.show_image()

    def show_image(self):
        if self.images:
            if hasattr(self, 'label'):
                self.label.pack_forget()
            self.label = Label(root, image=self.images[self.current_image])
            self.label.configure(width=self.images[self.current_image].width(),
                                 height=self.images[self.current_image].height())
            self.label.pack()

    def previous_image(self):
        if self.current_image > 0:
            self.current_image -= 1
            self.show_image()

    def next_image(self):
        if self.current_image < len(self.images) - 1:
            self.current_image += 1
            self.show_image()


root = Tk()
app = Application(master=root)
app.mainloop()
