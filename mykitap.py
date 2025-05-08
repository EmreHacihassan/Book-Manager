from PyQt6.QtWidgets import *
from kitap import Ui_Form
import sqlite3  # DB Bağlantısı


class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kitap = Ui_Form()
        self.kitap.setupUi(self)

        # Buton Tıklama Olayları
        self.kitap.btn_ekle.clicked.connect(self.kitapEkle)
        self.kitap.btn_listele.clicked.connect(self.bilgiListele)
        self.kitap.pushButton.clicked.connect(self.kitapsil) # silme işlemi
        self.kitap.btn_kitapgetir.clicked.connect(self.kitapgetir)
        self.kitap.btn_guncelle.clicked.connect(self.guncelle)
        
        # Genel Tanımlamalar
        self.bilgiListele() # sayfa yüklendiğinde cbb içi dolu gelsin
        self.adi = self.kitap.txt_kitapadi
        self.yili = self.kitap.dateEdit
        self.sayfa = self.kitap.spinBox_sayfa
        self.dili = self.kitap.comboBox_dili
        self.yayinevi = self.kitap.comboBox_yayinevi
        self.aciklama = self.kitap.txt_aciklama


    def DB_Baglanti(self):
        with sqlite3.connect("./arsivci.db") as con:
            kod = con.cursor() # Satırlar arasında kodları çalıştır
            kod.execute(""" create table if not exists tbl_kitap
            (idno INT, adi TEXT, yili TEXT, sayfa INT, 
            dili TEXT, yayinevi TEXT, aciklama TEXT) """)
            return con
    
    # textbox içindeki verileri temizle
    def temizle(self):
        from datetime import datetime
        self.adi.clear()
        self.aciklama.clear()
        self.yili.setDate(datetime.now()) # ???
        self.sayfa.setValue(10)
        
            
    def kitapEkle(self):
        from random import randint as rnd
        idno = rnd(100,999) # 100 - 999 arasında rasgele sayı üret
        try:
            con = self.DB_Baglanti()
            kod = con.cursor()
            kod.execute(f""" insert into tbl_kitap values 
            ({idno}, "{self.adi.text()}", "{self.yili.text()}"  ,
             {self.sayfa.value()}, "{self.dili.currentText()}"  ,
            "{self.yayinevi.currentText()}", "{self.aciklama.toPlainText()}")  """)
            con.commit()
            QMessageBox.information(self, "Kayıt", "Kayıt Başarılı")
            self.temizle() # Kayıt eklendikten sonra alanları temizle
            
        except Exception as hatakodu:
            QMessageBox.critical(self,"HATA", hatakodu )

    def bilgiListele(self):
        ara = self.kitap.comboBox
        ara.clear()  # Kayıtlar her seferinde aynısını yazmasın
        con = self.DB_Baglanti()
        kod = con.cursor()
        kod.execute(" select idno, adi from tbl_kitap order by idno ASC")
        for kayit in kod.fetchall():
            ara.addItem(str(kayit[0]) + "-" + str(kayit[1]))  # aradaki tire, silmede split ile ayraç olacak
            print(kayit)
    
    def kitapsil(self):
        try:
            bilgi = self.kitap.comboBox
            sil = bilgi.currentText().split("-")
            con = self.DB_Baglanti()
            kod = con.cursor()
            kod.execute(f" delete from tbl_kitap where idno={int(sil[0])} ")
            con.commit()
            QMessageBox.information(self, "Sil", "Kitap Silinmiştir.")
        except Exception as hatakodu:
            QMessageBox.critical(self, "HATA", "Hata Oluştu" + str(hatakodu))

    def kitapgetir(self):
        bilgi = self.kitap.comboBox
        getir = bilgi.currentText().split("-")
        con = self.DB_Baglanti()
        kod = con.cursor()
        kod.execute(f" select * from tbl_kitap where idno={int(getir[0])} ")
        gun = kod.fetchone()
        
        # txt yerlerine eklemek
        self.kitap.label_IDNO.setText(str(gun[0]))  # initte tanımlı olmadığı için
        self.adi.setText(gun[1])
        self.sayfa.setValue(gun[3])
        self.dili.setCurrentText(gun[4]) # combobox
        self.yayinevi.setCurrentText(gun[5])
        self.aciklama.setPlainText(gun[6])
    
    
    def guncelle(self):
        try:
            con = self.DB_Baglanti()
            kod = con.cursor()
            # adi, yili, sayfa, dili, yayinevi, aciklama
            kod.execute(f"""  update tbl_kitap set
                         adi="{self.adi.text()}", yili="{self.yili.text()}",
                         sayfa={self.sayfa.value()}, dili="{self.dili.currentText()}", 
                         yayinevi="{self.yayinevi.currentText()}",
                         aciklama="{self.aciklama.toPlainText()}"
                         where idno={int(self.kitap.label_IDNO.text())}  """)
            con.commit()
            QMessageBox.information(self,"Güncelle","Bilgiler Güncellenmiştir")
        except Exception as hatakodu:
            QMessageBox.critical(self,"HATA","Hata Kodu: " + str(hatakodu) )
            
        
        