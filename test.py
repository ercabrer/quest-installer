import sys
from PySide6.QtWidgets import (
    QApplication,
    QWizard,
    QWizardPage,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
)
from PySide6.QtCore import Qt


class IntroPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Introduction")
        self.setSubTitle("Welcome to the Mac-style Installer.")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("This wizard simulates a native macOS installation."))
        self.setLayout(layout)


class SetupPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Settings")
        self.setSubTitle("Configure your application.")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Select an option:"))
        layout.addWidget(QRadioButton("Install GLPK Solver (recommended)"))
        layout.addWidget(QRadioButton("Already installed GLPK solver"))
        layout.addWidget(QRadioButton("Do not install GLPK Solver"))
        self.setLayout(layout)


class ConclusionPage(QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTitle("Conclusion")
        self.setSubTitle("Finished.")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Installation complete."))
        self.setLayout(layout)


class MacWizard(QWizard):
    def __init__(self, parent=None):
        super().__init__(parent)

        # KEY PART: Set the style to MacStyle
        self.setWizardStyle(QWizard.WizardStyle.MacStyle)

        self.addPage(IntroPage())
        self.addPage(SetupPage())
        self.addPage(ConclusionPage())

        self.setWindowTitle("Installation")
        self.resize(600, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Optional: Set theme to light/dark
    # app.setStyle("macos")

    wizard = MacWizard()
    wizard.show()
    sys.exit(app.exec())
