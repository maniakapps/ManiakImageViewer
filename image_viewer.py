#!/usr/bin/env python
""" Short description of this Python module.
Longer description of this module.
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.
"""

__author__ = "ManiakApps"
__authors__ = ["ManuelPizano"]
__contact__ = "admin@maniakapps.com"
__copyright__ = "Copyright 2021, ManiakApps"
__credits__ = ["ManuelPizano"]
__date__ = "2021/07/27"
__deprecated__ = False
__email__ = "admin@maniakapps.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Testing"
__version__ = "0.0.1"

try:
    import getpass
    import PIL.Image
    import platform
    from Tkinter import *
    import tkFileDialog as fileDialog
    import PIL
    from PIL import ImageTk
    from screeninfo import get_monitors
except ImportError:
    from tkinter import *
    from tkinter import filedialog
    import PIL
    from PIL import ImageTk
    from screeninfo import get_monitors


class MainFrame(Frame):
    """
        Creates a MainFrame based on Frame class so we can use and display its own attributes.
    """

    def __init__(self, contenedor=None):
        """
        The constructor initializes a container receiving a Tk instance.
        :param contenedor: A Tk instance used to display the frame on it.
        """
        super().__init__(contenedor)

        # Getting the screen resolution
        self.resolution = get_monitors()
        self.width = self.resolution[0].width
        self.height = self.resolution[0].height

        # Widgets section
        self.im = None
        self.imagen = PhotoImage()
        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Abrir", command=self.abrir)
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.numero_pagina = 0
        self.num_imagen_sig = StringVar()
        Button(self, text="Abrir imagen", command=self.abrir).pack(side=LEFT)
        Button(self, text="Anterior", command=self.visualizar_anterior).pack(side=LEFT)
        Button(self, text="Siguiente", command=self.visualizar_siguiente).pack(side=LEFT)
        Label(self, textvariable=self.num_imagen_sig).pack(side=LEFT)
        self.pack(side=TOP, fill=BOTH)
        self.etiqueta = Label(self)
        self.etiqueta.pack()

    def cambiar_imagen(self):
        """
        Changes the background image in the self.etiqueta widget
        based on the image type either bitmap or a different type.
        """
        if self.im.mode == "1":  # bitmap image
            self.imagen = PIL.ImageTk.BitmapImage(self.im,
                                                  foreground="white")
        else:  # photo image
            self.imagen = PIL.ImageTk.PhotoImage(image=self.im)

        self.etiqueta.config(image=self.imagen,
                             bg="#000000",
                             width=self.width,
                             height=self.height)

    def abrir(self):
        """
        Promps the user with a FileDialog so he can choose the image to be open.
        It works for both Linux and Windows setting Documents as the first seeking folder
        Also updates the num of page label
        :return:
        """
        try:
            filename = ""
            user = getpass.getuser()
            if platform.system() == "Windows":
                filename = filedialog.askopenfilename(initialdir="C:/Users/%s" % user,
                                                      filetypes=[("Imagenes", "*.png *.jpg *.jpge")])
            elif platform.system() == "Linux":
                filename = filedialog.askopenfilename(initialdir="/home/%s/Documents" % user,
                                                      filetypes=[("Imagenes", "*.png *.jpg *.jpge")])

            if filename != "":

                self.im = PIL.Image.open(filename)
                w = self.im.width
                h = self.im.height
                if self.im.width > (self.width - (self.width // 3)):
                    w = (self.width // 3)
                if self.im.height > (self.im.height - (self.im.height // 3)):
                    h =self.height - (self.height // 6)
                size = (w, h)
                self.im = self.im.resize(size, resample=PIL.Image.BILINEAR)
            self.cambiar_imagen()
            self.numero_pagina = 0
            self.num_imagen_sig.set(str(self.numero_pagina + 1))
        except Exception as e:
            print("Se produjo un error")
            print(e)

    def visualizar_anterior(self):
        """
        Visualizes the previous image and updates the number
        :returns
        """
        pass

    def visualizar_siguiente(self):
        """
              Visualizes the next image and updates the number
              :returns
              """
        pass


class App(Tk):
    """
    Creates a Tk child were the App is built-on.
    """

    def __init__(self):
        """
        The constructor initializes the App title, and its properties.
        """
        super().__init__()
        # sets the window title
        self.title('Visualizador de Imagenes by ManiakApps')
        # Users cannot resize window neither width or height
        self.resizable(True, True)

        # getting the monitor 1 resolution, in case there are ore than one monitor list can be indexed
        self.resolution = get_monitors()
        self.width = self.resolution[0].width - 100
        self.height = self.resolution[0].height - 100

        # doing // 8 and // 4 on Linux due to errors
        self.geometry(f"{int(self.width * 0.80)}x{int(self.height * 0.80)}+{self.width // 8}-{self.height // 4}")


# The following part runs the code
if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()
