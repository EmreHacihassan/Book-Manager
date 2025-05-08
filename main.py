from PyQt6.QtWidgets import QApplication
from mykitap import Form
app = QApplication([])
window = Form()
window.showNormal() # tam ekran olarak aç
app.exec() # çalıştır