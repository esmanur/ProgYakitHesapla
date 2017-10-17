from PyQt4.QtGui import*
from PyQt4.QtCore import*

class yakitHesaplayicisi(QDialog):
     def __init__(self,ebeveyn=None):
         super(yakitHesaplayicisi,self).__init__(ebeveyn)

         izgara=QGridLayout()
         izgara.addWidget(QLabel('Gideceğiniz yol (KM):'),0,0)
         self.gidilenYol=QLineEdit()
         izgara.addWidget(self.gidilenYol,0,1)

         izgara.addWidget(QLabel('Fiyatı'),1,0)
         self.yakitFiyati=QLineEdit()
         izgara.addWidget(self.yakitFiyati,1,1)

         izgara.addWidget(QLabel("Tüketilen Yakıt: "),2,0)
         self.yakitTuketimi=QLineEdit()
         izgara.addWidget(self.yakitTuketimi,2,1)

         izgara.addWidget(QLabel('Toplam Tutar: '),3,0)
         self.tutar=QLabel('<font color="blue"><i>KM giriniz</i></font>')
         izgara.addWidget(self.tutar,3,1)

         hesaplaDugme=QPushButton('Hesapla')
         self.connect(hesaplaDugme, SIGNAL('pressed()'),self.yakitHesapla)
         izgara.addWidget(hesaplaDugme,4,0,1,2)

         self.setLayout(izgara)
         self.setWindowTitle('Yakıt Hesaplayıcısı')

     def yakitHesapla(self):
            yol=0
            try: yol=int(self.gidilenYol.text())
            except: pass
            fiyat=0
            try: fiyat=float(self.yakitFiyati.text())
            except: pass
            tuketim=0
            try: tuketim=float(self.yakitTuketimi.text())
            except: pass

            if not yol:
                self.tutar.setText('<font color="blue"><i>KM giriniz</i></font>')
                self.gidilenYol.setFocus()
            elif not fiyat:
                self.tutar.setText('<font color="blue"><i>Fiyat Giriniz</i></font>')
                self.yakitFiyati.setFocus()
            elif not tuketim:
                self.tutar.setText('<font color="blue"><i>Tüketim Giriniz</i></font>')
                self.yakitTuketimi.setFocus()
            else:
                tutar=fiyat*(yol*tuketim)/100
                self.tutar.setText('<font color="green"><b>%0.2f</b> TL</font>' %tutar)
                

uyg=QApplication([])
pencere=yakitHesaplayicisi()
pencere.show()
uyg.exec_()
