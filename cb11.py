import  tkinter as tk

root = tk.Tk()

root.title('lap trinh python')
root.geometry('300x300')

labe1 = tk.Label(root, text='Welcome to Tekmonk!')
labe1.pack(padx=20)

labe2 = tk.Label(root, text='Trinh ba quy' ,borderwidth=0,relief="solid" , width=30 )
labe2.pack(padx =20)

# labe3 = tk.Label(root, text='3' ,bg= "green" ,fg='white')
# labe3.grid(column=3,row=0,padx =5 , pady=40)
#
labe4 = tk.Label(root, text='Login' ,bg= "blue" ,fg='white',pady=1,width=20)
labe4.pack( padx =40)
#
# labe5 = tk.Label(root, text='5' ,bg= "green" ,fg='white')
# labe5.grid(column=5,row=0,padx =5 , pady=80)


root.mainloop()