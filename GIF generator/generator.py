#importing libraires/modules
from tkinter import *
from tkinter import messagebox
import glob
import imageio

#user input design
wn = Tk()
wn.title("GIF CREATOR")
wn.geometry('500x300')
wn.config(bg='azure')

#creates the path for input folderv and its extensions.
extension = StringVar(wn)
direc = StringVar(wn)

#main label design
Label(wn, text="GIF CREATOR", bg='azure',fg='black', font=('Times', 20,'bold')).place(x=60, y=10)

#get extension of the imgage as png or jpeg
Label(wn, text='Please select the extension of the images',bg='azure2', anchor="e", justify=LEFT).place(x=20, y=70)

Radiobutton(wn, text='png',bg='azure2', variable=extension, value='png').place(x=50,y=100)
Radiobutton(wn, text='jpeg',bg='azure2',variable=extension, value='jpeg').place(x=150,y=100)

#get the apth for input folder with images
Label(wn, text='Please enter the folder location where images exist',bg='azure2', anchor="e", justify=LEFT).place(x=20, y=130)

Entry(wn,textvariable=direc, width=35, font=('calibre',10,'normal')).place(x=200,y=160)

#button to convert image to gifs.
Label(wn, text='Please click the button to get the GIF', bg='azure2',anchor="e", justify=LEFT).place(x=20, y=190)

Button(wn, text="Click Me", bg='ivory3',font=('calibre', 13), command= 'convertToGIF').place(x=230, y=220)

#run the program interface window till user close it.
wn.mainloop()

#now we are creating the functions for the program.
#function to convert images to gifs.
def convertToGIF():
    path = direc.get() #Get the path of the folder entered by the user
    ext=extension.get() #Get the extension png or jpeg
    path_in =path+'/*.'+ext #Creating the final path of the images
    path_out = path+"/MyGif.gif" #Creating the path for GIF in the sam

    imgs = []
    try:
        file = glob.glob(path_in, recursive = True) #Recursively getting 
        for im in file:
            imgs.append(imageio.imread(im))
        imageio.mimsave(path_out, imgs) #Converting the images to GIF 
        #Showing the message box on saving the gif
        messagebox.showinfo("DataFlair GIF Generator","GIF is saved successfully in the folder with Im")
    except:
        #Showing a message if not able to collect the images or convert them to 
        messagebox.showinfo("Error occurred!","Please check the path of the folder ")



