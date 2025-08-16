import sys
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

def check_tor():
    try:
        socket.create_connection(("127.0.0.1", 9050), timeout=2)
        return "Tor Durumu: Bağlı ✅"
    except:
        return "Tor Durumu: Bağlı değil ❌"

class TorStatusApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tor Durumu Göstergesi")
        self.setGeometry(300, 300, 300, 100)

        self.label = QLabel(check_tor(), self)
        self.button = QPushButton("Yenile", self)
        self.button.clicked.connect(self.refresh_status)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def refresh_status(self):
        self.label.setText(check_tor())

app = QApplication(sys.argv)
window = TorStatusApp()
window.show()
sys.exit(app.exec_())
