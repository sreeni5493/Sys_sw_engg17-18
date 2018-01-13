 
import sys
from PyQt4.QtGui import QApplication, QWidget
from Welcome import Ui_Welcome
from Editor import Ui_Form
from SmartFridge import Ui_Form
from Sudoku import Ui_Form

app = QApplication(sys.argv)
window = QWidget()
ui = Ui_Welcome()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
