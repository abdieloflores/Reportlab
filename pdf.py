# -*- coding: utf-8 -*-
import pymysql
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

#Licencias Base de Datos
_host='localhost'
_user='root'
_password='gafo951101'
_db='PuntoVenta'

class NOTA():
    def __init__(self):
        self.nombreNota = "Nota-1"
        self.documento = canvas.Canvas("%s.pdf" % (self.nombreNota),pagesize=letter) #Instancia de la clase canvas poniendo nombre al archivo
        self.documento.setTitle("Nota de Venta")
        self.w, self.h = letter

    def encabezado(self):
        nombre = "TIENDA DON LUIS"
        rfc = "XXXX010101"
        calle ="Av. Plan de San Luis"
        ext ="1820"
        inte = " "
        col = "Chapultepec Country"
        cp = "44620"
        ciudad = "Guadalajara"
        estado = "Jalisco"
        pais = "México"
        self.documento.setStrokeColorRGB(.6588,0,.0627)
        self.documento.setFillColorRGB(.6588,0,.0627)
        self.documento.rect(0,672,612, 120,fill=True,stroke=False)

        self.documento.drawImage("logo.png", self.w-170, 710, width=120, height=60)

        self.documento.setFillColorRGB(1,1,1)
        self.documento.setFont("Helvetica", 12)
        cabecera = self.documento.beginText(50, 760)
        cabecera.textLines("%s\n%s\nAv. %s No.%s Int.%s\nCol. %s, C.P. %s\n%s, %s, %s." % (nombre, rfc, calle, ext, inte, col, cp, ciudad, estado, pais))
        self.documento.drawText(cabecera)

    def clienteNota(self):
        nombre = "ABDIEL OTONIEL FLORES GONZALEZ"
        rfc = "XXXX010101"
        calle ="Av. Plan de San Luis"
        ext ="1820"
        inte = " "
        col = "Chapultepec Country"
        cp = "44620"
        ciudad = "Guadalajara"
        estado = "Jalisco"
        pais = "México"
        codigoNota = "Nota-1"
        fechaHora = "13/04/2020 13:12:32"
        self.documento.setFillColorRGB(.2196,.2196,.2196)
        self.documento.setFont("Helvetica", 12)
        cliente = self.documento.beginText(50, 630)
        cliente.textLines("%s\n%s\nAv. %s No.%s Int.%s\nCol. %s, C.P. %s\n%s, %s, %s." % (nombre, rfc, calle, ext, inte, col, cp, ciudad, estado, pais))
        self.documento.drawText(cliente)

        self.documento.setFillColorRGB(.6588,0,.0627)
        self.documento.setFont("Helvetica-Bold", 15)
        self.documento.drawRightString(self.w-50,630,"%s" %(codigoNota))
        self.documento.setFillColorRGB(.2196,.2196,.2196)
        self.documento.setFont("Helvetica-Bold", 12)
        self.documento.drawRightString(self.w-50,590,"Fecha y Hora:")
        self.documento.setFont("Helvetica", 12)
        self.documento.drawRightString(self.w-50,575,"%s" % (fechaHora))

    def hacerTabla(self):
        datos = [["CANTIDAD","NOMBRE","P/U","TOTAL"],
                ["1","Producto2","750","1500"],
                ["1","Producto3","750","1500"],
                ["1","Producto4","750","1500"],
                ["1","Producto5","750","1500"],
                ["1","Producto6","750","1500"],
                ["1","Producto7","750","1500"],
                ["1","Producto8","750","1500"],
                ["1","Producto9","750","1500"],
                ["1","Producto10","750","1500"],
                ["1","Producto11","750","1500"],
                ["1","Producto12","750","1500"],
                ["1","Producto13","750","1500"],
                ["1","Producto14","750","1500"],
                ["1","Producto15","750","1500"],
                ["1","Producto16","750","1500"],
                ["1","Producto17","750","1500"],
                ["1","Producto18","750","1500"],
                ["1","Producto19","750","1500"],
                ["1","Producto20","750","1500"],
                ["1","Producto21","750","1500"],
                ["1","Producto22","750","1500"],
                ["1","Producto23","750","1500"],
                ["1","Producto24","750","1500"],
                ["1","Producto25","750","1500"],
                ["1","Producto26","750","1500"],
                ["1","Producto27","750","1500"],
                ["1","Producto28","750","1500"],
                ["1","Producto28","750","1500"],
                [" "," ","TOTAL:","50,000.00"]]
        tabla = Table(datos)
        tabla.setStyle(TableStyle([ ('BACKGROUND',(1,1),(-2,-2),colors.green),
                                ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))


    def guardar(self):
        self.documento.showPage()
        self.documento.save() #Guardar documento
    
    def go(self):
        self.encabezado()
        self.clienteNota()
        self.guardar()


if __name__ == "__main__":
    nota = NOTA()
    nota.go()



