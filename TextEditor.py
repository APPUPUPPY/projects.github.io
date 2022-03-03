#*************************************************

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
from urllib import request

#*************************************************

def change_colour():
    color = colorchooser.askcolor(title="Pick a color to use!")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("New file")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"),
                                                          ("Text Documents", "*.txt")])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except Exception:
        print("couldn't read file")

    finally:
        file.close()

#Function to save a file to a drive from TextEditor
def save_file():
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("Coudn't save file")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def clear_all():
    text_area.delete(1.0, END)


def select_all(e):
    text_area.tag_add('sel', '1.0', 'end')


def about():
    showinfo("About this program", "This is a software made by KrisXD\n "
                                   "If you are struggling with the software\n"
                                   "Feel Free to contact KrisXD.\n\n"
                                   "This software is still in development, Some of the features are disabled\n"
                                   "To enable it, you need to manually edit the code and enable it.")


def contact():
    showinfo("Contact KrisXD", "Discord: @KrisXD#0065\n "
             "Telegram: @KrisGamingXD\n\n "
             "Thanks for using TextEditor")


def media():
    request.urlopen('https://www.youtube.com/channel/UC-gxvgju2PI9EJ7jPb3knJA')


def night_on():
    pass


def night_off():
    pass


def quit():
    window.destroy()


#*************************************************

window = Tk()
window.iconbitmap('https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Ftext-editor-icon-trendy-logo-concept-white-backg-background-technology-collection-suitable-use-web-apps-mobile-131195539.jpg&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Ftext-editor-icon-trendy-logo-concept-white-backg-background-technology-collection-suitable-use-web-apps-mobile-image131195539&tbnid=C7GlqF4THtbv3M&vet=10CAMQxiAoAGoXChMI8MbdxIH89QIVAAAAAB0AAAAAEA0..i&docid=eHR9sShkcvleWM&w=800&h=800&itg=1&q=text%20editor&ved=0CAMQxiAoAGoXChMI8MbdxIH89QIVAAAAAB0AAAAAEA0')
window.title("Text Editor")
file = None

window_width = 700
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("20")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

#color_button = Button(frame, text="Color", command=change_colour)
#color_button.grid(row=0, column=0)

arrow1 = Button(frame, text="Change font -->")
arrow1.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

arrow2 = Button(frame, text="<-- Change font size")
arrow2.grid(row=0, column=3)

#*************************************************

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save as", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Color", command=change_colour)
#view_menu.add_command(label="Select all", command=select_all)
view_menu.add_command(label="Clear all", command=clear_all)
view_menu.add_separator()
view_menu.add_command(label="Dark mode(OFF)", command=night_on)
view_menu.add_command(label="Light mode(OFF)", command=night_on)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Contact", command=contact)
#help_menu.add_command(label="Media help", command=media)
help_menu.add_separator()
help_menu.add_command(label="Exit", command=quit)

#*************************************************

window.mainloop()

#*************************************************