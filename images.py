from tkinter import *
from PIL import ImageTk,Image #for importing images 
root=Tk()
root.title('image slider') #title for page 
root.iconbitmap("ico.ico") #logo/ICON we must have to use the ICONBITMAP
my_img=ImageTk.PhotoImage(Image.open("pngs/1-men-hair-png-image.png")) #importing images
my_img1=ImageTk.PhotoImage(Image.open("pngs/2-2-whatsapp-free-png-image.png"))
my_img2=ImageTk.PhotoImage(Image.open("pngs/2-2-motorcycle-png.png"))
my_img3=ImageTk.PhotoImage(Image.open("pngs/5-moto-png-image-motorcycle-png_400x400.png"))
my_img4=ImageTk.PhotoImage(Image.open("pngs/80551-united-trump-humour-states-donald-cartoon-man.png"))
my_img6=ImageTk.PhotoImage(Image.open("pngs/big.png"))
my_img5=ImageTk.PhotoImage(Image.open("pngs/58613-emotion-love-mood-angry-anger-whatsapp.png"))



image_list=[my_img,my_img1,my_img2,my_img3,my_img4,my_img5,my_img6] #adding images to the list
   
status=Label(root,text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#to print the status of watching the grid   
#status.grid(row=2,column=0,columnspan=3,sticky=W+E)

my_label=Label(image=my_img) #to represent on the screen
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    if image_number ==len(image_list):
        button_forward=Button(root,text=">>",state=DISABLED)
    
    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status=Label(root,text="Image " +str(image_number)+ " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#to print the status of watching the grid   
    status.grid(row=2,column=0,columnspan=3,sticky=E)



def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==1:
        button_back=Button(root,text="<<",state=DISABLED)
        

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    status=Label(root,text="Image " +str(image_number)+ " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#to print the status of watching the grid   
    status.grid(row=2,column=0,columnspan=3,sticky=E)

    
   
button_back=Button(root,text="<<",command=back)
button_exit=Button(root,text="EXIT ! PROGRAM",fg="red",command=root.destroy)
button_forward=Button(root,text=">>",command=lambda:forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)



root.mainloop()
