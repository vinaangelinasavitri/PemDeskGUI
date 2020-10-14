from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget, QLabel, QCheckBox, QRadioButton
from PyQt5.QtGui import QColor

if __name__ == "__main__":

    app = QApplication([])
    form = QWidget()
    form.setGeometry(100, 100, 500, 500)
    form.setWindowTitle("Contoh Input Biodata")

    label = QLabel(form)
    label.setText("Input Biodata")
    label.setStyleSheet("background-color: rgb(176, 196, 222); color: red; font: bold Times New Roman; font-size: 50px;")

    lineEdit = QLineEdit()
    lineEdit2 = QLineEdit()
    lineEdit3 = QLineEdit()

    layout = QFormLayout()
    layout.addRow(label)
    layout.addRow("Name", lineEdit)
    layout.addRow("Address", lineEdit2)
    layout.addRow("", lineEdit3)

    checkBox = QCheckBox("Makan")
    checkBox2 = QCheckBox("Tidur")
    checkBox3 = QCheckBox("Main")
    layout.addRow("Hobby", checkBox)
    layout.addWidget(checkBox2)
    layout.addWidget(checkBox3)

    rad = QRadioButton("Pelajar")
    rad2 = QRadioButton("Pegawai")
    rad3 = QRadioButton("Wiraswasta")
    layout.addRow("Status", rad)
    layout.addWidget(rad2)
    layout.addWidget(rad3)

    form.setLayout(layout)

    form.show()
    app.exec_()




