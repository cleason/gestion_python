from tkinter import *
from PIL import Image, ImageTk
from datetime import *
import time
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau de bord")
        self.root.geometry("1366x768")
        self.root.config(bg="#eff5f6")
        
        icon = PhotoImage(file=r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\pic-icon.png")
        self.root.iconphoto(True,icon)
        
        # En-tête
        self.entete =  Frame(self.root, bg="#009df4")
        self.entete.place(x=300, y=0, width=1070, height=60)
        
        self.deconnect = Button(self.entete, text="Deconnecter", bg="#32cf8e", font=("poppins", 13, "bold"), bd=0, fg="white", cursor="hand2", activebackground="#32cf8e")
        self.deconnect.place(x=925, y=15)
        
        #Menu
        self.FrameMenu = Frame(self.root, bg="#fff")
        self.FrameMenu.place(x=0, y=0, width=300, height=750)
        
        self.logoImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\hyy.png")
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.FrameMenu, image=photo, bg="#fff")
        self.logo.image = photo
        self.logo.place(x=70, y=80)        
        self.Nom = Label(self.FrameMenu, text="Cléason Noglo", bg="#fff", font=("poppins", 13, "bold"))
        self.Nom.place(x=80, y=200)
        
        #Tableau de bord
        self.dashboardImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\dashboard-icon.png")
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.FrameMenu, image=photo, bg="#fff")
        self.dashboard.image = photo
        self.dashboard.place(x=35, y=289)
        self.dashboard_text = Button(self.FrameMenu, text="Tableau de bord", bg="#fff", font=("poppins", 13, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.dashboard_text.place(x=80, y=289)
        
        #Gestion
        self.gestionImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\manage-icon.png")
        photo = ImageTk.PhotoImage(self.gestionImage)
        self.gestion = Label(self.FrameMenu, image=photo, bg="#fff")
        self.gestion.image = photo
        self.gestion.place(x=35, y=340)
        self.gestion_text = Button(self.FrameMenu, text="Gestion", bg="#fff", font=("poppins", 13, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.gestion_text.place(x=80, y=345)
        
        
        #parametres
        self.parametreImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\settings-icon.png")
        photo = ImageTk.PhotoImage(self.parametreImage)
        self.parametre = Label(self.FrameMenu, image=photo, bg="#fff")
        self.parametre.image = photo
        self.parametre.place(x=35, y=402)
        self.parametre_text = Button(self.FrameMenu, text="Parametres", bg="#fff", font=("poppins", 13, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.parametre_text.place(x=80, y=402)
        
        #Quitter
        self.quitterImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\exit-icon.png")
        photo = ImageTk.PhotoImage(self.quitterImage)
        self.quitter = Label(self.FrameMenu, image=photo, bg="#fff")
        self.quitter.image = photo
        self.quitter.place(x=25, y=452)
        self.quitter_text = Button(self.FrameMenu, text="Quitter", bg="#fff", font=("poppins", 13, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.quitter_text.place(x=85, y=462)
        
        #Corps
        self.titre = Label(self.root, text="Tableau de bord",font=("poppins", 13, "bold"), fg="#0064d3", bg="#eff5f6")
        self.titre.place(x=325, y=70)
        
        #Corps1
        self.corp1 = Frame(self.root, bg="#fff")
        self.corp1.place(x=328, y=110, width=1040, height=350)
        
        donnee = pd.read_excel(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\donnee.xlsx")
        sumlundi = sum(donnee["Lundi"])
        summardi = sum(donnee["Mardi"])
        summercredi = sum(donnee["Mercredi"])
        sumjeudi = sum(donnee["Jeudi"])
        sumvendredi = sum(donnee["Vendredi"])
        sumsamedi = sum(donnee["Samedi"])
        
        fig = plt.figure(figsize=(5,5), dpi=100)
        fig.set_size_inches(5, 3.5)
        
        labels = "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"
        sizes = [sumlundi, summardi, summercredi, sumjeudi, sumvendredi, sumsamedi]
        colors = ["yellowgreen", "gold", "lightcoral", "lightskyblue", "cyan", "red"]
        explode = (0.2, 0, 0, 0, 0, 0)
        
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        
        plt.axis("equal")
        
        canvasbar = FigureCanvasTkAgg(fig, master=self.root)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=1120, y=285, anchor=CENTER)
        
        #Diagramme
        fig = plt.figure(figsize=(5, 3.5), dpi=100)
        labels = "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"
        labelpos = np.arange(len(labels))
        semainesum = [sumlundi, summardi, summercredi, sumjeudi, sumvendredi, sumsamedi]
        
        plt.bar(labelpos, semainesum, align="center", alpha=1.0)
        plt.xticks(labelpos, labels)
        plt.ylabel("Prix")
        plt.ylabel("Semaine")
        plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
        plt.title("Vente de la semaine")
        plt.xticks(rotation=30, horizontalalignment='center')
        
        for index, datapoints in enumerate(semainesum):
            plt.text(x=index, y=datapoints+0.3, s=f"{datapoints}", fontdict=dict(fontsize=10), ha="center", va="bottom")
            
        canvasbar = FigureCanvasTkAgg(fig, master=self.root)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=600, y=285, anchor=CENTER)
        
        self.root.protocol("WM_DELETE_WINDOW", self.Exit)
        
        #Corps2
        self.corp2 = Frame(self.root, bg="#009aa5")
        self.corp2.place(x=328, y=495, width=310, height=220)
        
        self.totalclientImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\left-icon.png")
        photo = ImageTk.PhotoImage(self.totalclientImage)
        self.totalclient = Label(self.corp2, image=photo, bg="#009aa5")
        self.totalclient.image = photo
        self.totalclient.place(x=220, y=0)
        
        self.ntotalclient_text = Button(self.corp2, text="300", bg="#009aa5", fg="white", font=("poppins", 25, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.ntotalclient_text.place(x=120, y=100)
        
        self.ttotalclient_text = Button(self.corp2, text="Total Client", bg="#009aa5", fg="white", font=("poppins", 15, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.ttotalclient_text.place(x=5, y=5)
        
        #Corps3
        self.corps3 = Frame(self.root, bg="#e21f26")
        self.corps3.place(x=680, y=495, width=310, height=220)
        
        self.totalemployeImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\left-icon.png")
        photo = ImageTk.PhotoImage(self.totalemployeImage)
        self.totalemploye = Label(self.corps3, image=photo, bg="#e21f26")
        self.totalemploye.image = photo
        self.totalemploye.place(x=220, y=0)
        
        self.ntotalemploye_text = Button(self.corps3, text="20", bg="#e21f26", fg="white", font=("poppins", 25, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.ntotalemploye_text.place(x=120, y=100)
        
        self.ttotalemploye_text = Button(self.corps3, text="Total Employe", bg="#e21f26", fg="white", font=("poppins", 15, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.ttotalemploye_text.place(x=5, y=5)
        
        #Corps4
        self.corps4 = Frame(self.root, bg="#ffcb1f")
        self.corps4.place(x=1030, y=495, width=310, height=220)
        
        self.totalventeImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\earn3.png")
        photo = ImageTk.PhotoImage(self.totalventeImage)
        self.totalvente = Label(self.corps4, image=photo, bg="#ffcb1f")
        self.totalvente.image = photo
        self.totalvente.place(x=220, y=0)
        
        self.ntotalvente_text = Button(self.corps4, text="450.000", bg="#ffcb1f", fg="#000000", font=("poppins", 25, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.ntotalvente_text.place(x=80, y=100)
        
        self.ttotalvente_text = Button(self.corps4, text="Total Vente", bg="#ffcb1f", fg="#000000", font=("poppins", 15, "bold"), bd=0, cursor="hand2", activebackground="#fff")
        self.ttotalvente_text.place(x=8, y=5)
        
        
        #Heures
        self.heureImage = Image.open(r"C:\Users\Admin\OneDrive\Bureau\codePython\gestion_python\Image_DashBoard\time.png")
        photo = ImageTk.PhotoImage(self.heureImage)
        self.heure = Label(self.FrameMenu, image=photo, bg="#fff")
        self.heure.image = photo
        self.heure.place(x=78, y=20)
        
        self.heures_text = Label(self.FrameMenu)
        self.heures_text.place(x=115, y=15)
        self.afficher_heures()
        
    def afficher_heures(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime("%d/%m/%Y")
        resultat = f"{self.date}\n{self.time}"
        self.heures_text.config (text=resultat, bd=0, font=("poppins", 13, "bold"), bg="#fff")
        self.heures_text.after(100, self.afficher_heures)
        
    def Exit(self):
        self.root.quit()





if __name__ == "__main__":
    root = Tk()
    Dashboard(root)
    root.mainloop()