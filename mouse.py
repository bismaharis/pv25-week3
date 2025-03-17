import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QRect

class MouseTrack(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Tugas 3_F1D022055_Lalu Bisma Kurniawan Haris")
    self.setGeometry(100, 100, 800, 600)  
    
    # Label
    self.label = QLabel("Catch Me If You Can", self)
    self.label.setAlignment(Qt.AlignCenter)
    self.label.setFixedSize(200, 50)
    self.center_label()
    

    self.setMouseTracking(True)
    self.label.setMouseTracking(True)

  def center_label(self):
    """Center the label in the window"""
    window_width = self.width()
    window_height = self.height()
    label_width = self.label.width()
    label_height = self.label.height()
    
    center_x = (window_width - label_width) // 2
    center_y = (window_height - label_height) // 2
    
    self.label.move(center_x, center_y)

  def mouseMoveEvent(self, event):
    """Handle mouse movement events"""
    coords = f"X: {event.x()}, Y: {event.y()}"
    self.label.setText(coords)
    
    # Hover Check
    if self.label.geometry().contains(event.pos()):
      self.move_random()

  def move_random(self):
    """Move label to a random position within window"""
    window_width = self.width()
    window_height = self.height()
    label_width = self.label.width()
    label_height = self.label.height()
    
    max_x = window_width - label_width
    max_y = window_height - label_height - 30  
    
    new_x = random.randint(0, max_x)
    new_y = random.randint(0, max_y)
    
    self.label.move(new_x, new_y)

  def resizeEvent(self, event):
    """Handle window resize to keep label within bounds"""
    current_pos = self.label.pos()
    max_x = self.width() - self.label.width()
    max_y = self.height() - self.label.height() - 30
    
    if current_pos.x() > max_x:
      current_pos.setX(max_x)
    if current_pos.y() > max_y:
      current_pos.setY(max_y)
    if current_pos.x() < 0:
      current_pos.setX(0)
    if current_pos.y() < 0:
      current_pos.setY(0)
        
    self.label.move(current_pos)
    super().resizeEvent(event)

def main():
  app = QApplication(sys.argv)
  window = MouseTrack()
  window.show()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()