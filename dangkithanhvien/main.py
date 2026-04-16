import sys
import re
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QRadioButton, 
                             QButtonGroup, QCheckBox, QPushButton, QMessageBox, 
                             QStackedWidget, QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt6.QtCore import Qt
import database

class RegistrationForm(QWidget):
    def __init__(self, parent=None, member_id=None):
        super().__init__(parent)
        self.member_id = member_id
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 20, 50, 20)
        layout.setSpacing(15)

        # Title
        title_label = QLabel("Đăng ký")
        title_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        layout.addWidget(title_label)

        sub_title = QLabel("Nhanh chóng và dễ dàng")
        sub_title.setStyleSheet("color: gray; font-size: 14px;")
        layout.addWidget(sub_title)

        # Name row
        name_layout = QHBoxLayout()
        self.ho_input = QLineEdit()
        self.ho_input.setPlaceholderText("Họ")
        self.ten_input = QLineEdit()
        self.ten_input.setPlaceholderText("Tên")
        name_layout.addWidget(self.ho_input)
        name_layout.addWidget(self.ten_input)
        layout.addLayout(name_layout)

        # Email/Phone
        self.contact_input = QLineEdit()
        self.contact_input.setPlaceholderText("Số di động hoặc email")
        layout.addWidget(self.contact_input)

        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu mới")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Birthday
        layout.addWidget(QLabel("Ngày sinh"))
        birth_layout = QHBoxLayout()
        
        self.day_cb = QComboBox()
        self.day_cb.addItems([str(i) for i in range(1, 32)])
        
        self.month_cb = QComboBox()
        self.month_cb.addItems([f"Tháng {i}" for i in range(1, 13)])
        
        self.year_cb = QComboBox()
        self.year_cb.addItems([str(i) for i in range(1900, 2025)])
        self.year_cb.setCurrentText("1970")

        birth_layout.addWidget(self.day_cb)
        birth_layout.addWidget(self.month_cb)
        birth_layout.addWidget(self.year_cb)
        layout.addLayout(birth_layout)

        # Gender
        layout.addWidget(QLabel("Giới tính"))
        gender_layout = QHBoxLayout()
        self.gender_group = QButtonGroup(self)
        self.male_rb = QRadioButton("Nam")
        self.female_rb = QRadioButton("Nữ")
        self.gender_group.addButton(self.male_rb)
        self.gender_group.addButton(self.female_rb)
        gender_layout.addWidget(self.male_rb)
        gender_layout.addWidget(self.female_rb)
        gender_layout.addStretch()
        layout.addLayout(gender_layout)

        # Terms
        self.terms_cb = QCheckBox("Tôi đồng ý với các điều khoản trên")
        layout.addWidget(self.terms_cb)

        # Submit button
        self.submit_btn = QPushButton("Đăng ký")
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #00a400;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #008a00;
            }
        """)
        self.submit_btn.clicked.connect(self.handle_submit)
        layout.addWidget(self.submit_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def validate_password(self, password):
        if len(password) < 8:
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

    def handle_submit(self):
        ho = self.ho_input.text()
        ten = self.ten_input.text()
        contact = self.contact_input.text()
        password = self.password_input.text()
        birthday = f"{self.day_cb.currentText()} {self.month_cb.currentText()} {self.year_cb.currentText()}"
        gender = "Nam" if self.male_rb.isChecked() else "Nữ" if self.female_rb.isChecked() else ""
        
        if not all([ho, ten, contact, password, gender]) or not self.terms_cb.isChecked():
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin và đồng ý điều khoản!")
            return

        if not self.validate_password(password):
            QMessageBox.warning(self, "Lỗi mật khẩu", "Mật khẩu phải ít nhất 8 ký tự, gồm chữ hoa, chữ thường, số và ký tự đặc biệt!")
            return

        try:
            if self.member_id:
                database.update_member(self.member_id, ho, ten, contact, password, birthday, gender)
                QMessageBox.information(self, "Thành công", "Cập nhật thông tin thành công!")
            else:
                database.add_member(ho, ten, contact, password, birthday, gender)
                QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
            
            # Switch to list view
            self.parent().parent().switch_to_list()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Có lỗi xảy ra: {str(e)}")

class MemberListForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        title = QLabel("Danh sách thành viên")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Họ", "Tên", "Liên hệ", "Mật khẩu", "Ngày sinh", "Giới tính"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        self.refresh_btn = QPushButton("Làm mới")
        self.refresh_btn.clicked.connect(self.load_data)
        
        self.edit_btn = QPushButton("Sửa")
        self.edit_btn.clicked.connect(self.handle_edit)
        
        self.delete_btn = QPushButton("Xóa")
        self.delete_btn.setStyleSheet("background-color: #d9534f; color: white;")
        self.delete_btn.clicked.connect(self.handle_delete)

        self.add_new_btn = QPushButton("Thêm mới")
        self.add_new_btn.clicked.connect(lambda: self.parent().parent().switch_to_register())

        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addWidget(self.add_new_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        members = database.get_all_members()
        self.table.setRowCount(0)
        for row_idx, member in enumerate(members):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(member):
                item = QTableWidgetItem(str(data))
                self.table.setItem(row_idx, col_idx, item)

    def handle_delete(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một thành viên để xóa!")
            return
        
        member_id = self.table.item(current_row, 0).text()
        reply = QMessageBox.question(self, "Xác nhận", "Bạn có chắc muốn xóa thành viên này?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            database.delete_member(member_id)
            self.load_data()

    def handle_edit(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một thành viên để sửa!")
            return
        
        # Get data
        data = []
        for i in range(7):
            data.append(self.table.item(current_row, i).text())
        
        self.parent().parent().switch_to_edit(data)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý thành viên")
        self.resize(800, 600)
        database.init_db()
        
        self.stacked_widget = QStackedWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

        self.register_view = RegistrationForm(self.stacked_widget)
        self.list_view = MemberListForm(self.stacked_widget)

        self.stacked_widget.addWidget(self.register_view)
        self.stacked_widget.addWidget(self.list_view)

    def switch_to_list(self):
        self.list_view.load_data()
        self.stacked_widget.setCurrentWidget(self.list_view)

    def switch_to_register(self):
        # Create new form to clear data
        self.register_view = RegistrationForm(self.stacked_widget)
        self.stacked_widget.addWidget(self.register_view)
        self.stacked_widget.setCurrentWidget(self.register_view)

    def switch_to_edit(self, data):
        # Pre-fill data
        form = RegistrationForm(self.stacked_widget, member_id=data[0])
        form.ho_input.setText(data[1])
        form.ten_input.setText(data[2])
        form.contact_input.setText(data[3])
        form.password_input.setText(data[4])
        
        # Birthday parsing (simple space split)
        parts = data[5].split(' ')
        if len(parts) == 3:
            form.day_cb.setCurrentText(parts[0])
            form.month_cb.setCurrentText(parts[1])
            form.year_cb.setCurrentText(parts[2])
        
        if data[6] == "Nam":
            form.male_rb.setChecked(True)
        else:
            form.female_rb.setChecked(True)
            
        form.submit_btn.setText("Cập nhật")
        self.stacked_widget.addWidget(form)
        self.stacked_widget.setCurrentWidget(form)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
