import tkinter as tk
from PIL import ImageTk, Image

class IntroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App Intro")
        self.root.configure(bg="black")
        self.root.overrideredirect(True)
        
     
        self.logo_image = ImageTk.PhotoImage(Image.open("logo.png"))
        self.logo_label = tk.Label(self.root, image=self.logo_image, bg="black")
        self.logo_label.pack()
        
     
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        
        x = (screen_width - self.logo_image.width()) // 2
        y = (screen_height - self.logo_image.height()) // 2
        self.root.geometry(f"+{x}+{y}")
        
  
        self.root.after(3000, self.close_window)
        
    def close_window(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = IntroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
