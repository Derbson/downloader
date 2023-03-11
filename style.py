import qdarktheme

qss = """
    QPushButton[cssClass="specialButton"] {
        color: #fff;
        background: #0fd371;
    }
    QPushButton[cssClass="specialButton"]:hover {
        color: #fff;
        background: #129051;
    }
    QPushButton[cssClass="specialButton"]:pressed {
        color: #fff;
        background: #145c35;
    }
"""

def setupTheme():
    qdarktheme.setup_theme(
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": "#0fd371",
            },
            "[light]": {
                "primary": "#0fd371",
            },
        },
        additional_qss=qss
    )
