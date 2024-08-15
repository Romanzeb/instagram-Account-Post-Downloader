import instaloader
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

def download_post():
    #kullanıcı adı alma
    username = entry_username.get()

    try:
        #nesne oluşturma
        bot = instaloader.Instaloader()

        #profil nesne oluşturma 
        profile = instaloader.Profile.from_username(bot.context,username)
        #kullanıcının gönderilerini al
        posts = profile.get_posts()
        #gönderileri indir

        for index,post in enumerate(posts,1):
            bot.download_post(post,target=f"{profile.username}_{index}")
        #başarı mesajı
        messagebox.showinfo("Posts are Downloaded","Successfully") 
    except Exception as e:
        messagebox.showerror("Erorr:",str(e))

#genel arayüz

inst_appwindow = tk.Tk()
inst_appwindow.title("Instagram Post Loader")
inst_appwindow.geometry("300x250")
inst_appwindow.resizable(0,0)

Enter_TAG = tk.Label(inst_appwindow,text="Enter the Username :")
entry_username = tk.Entry(inst_appwindow,width=40)
Enter_button = tk.Button(inst_appwindow,width=10,text="Download",command=download_post)

Image_path = "instagram logo.jpg"
Img = Image.open(Image_path)
Img = Img.resize((100,100))
photo = ImageTk.PhotoImage(Img)
Image_label = tk.Label(inst_appwindow,image=photo)

Enter_button.grid(row=3,column=0)
entry_username.grid(row=2,column=0,padx=25,pady=25)
Enter_TAG.grid(row=1,column=0,padx=10,pady=10)
Image_label.grid(row=0, column=0)

inst_appwindow.mainloop()

