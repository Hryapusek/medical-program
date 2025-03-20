import sys

from dotenv import load_dotenv

from PyQt5 import QtWidgets

from main_window import MainWindow
from database_api.schema import init_db
from database_api.schema import Doctor

if __name__ == '__main__':
    load_dotenv()
    init_db()
    from sqlalchemy.orm import sessionmaker
    from database_api.engine import main_engine
    from database_api.schema import Doctor

    # Create a new session
    Session = sessionmaker(bind=main_engine)
        # Example: Insert a new doctor
    from sqlalchemy import insert, update

    # Using SQLAlchemy's insert construct to build an expression
    insert_stmt = insert(Doctor).values(
        first_name="John",
        last_name="Doe",
        specialty="Cardiology",
        contact_number="1234567890",
        email="johndoe@example.com",
        office_number="101"
    )

    update_stmt = update(Doctor).where(Doctor.first_name == "John").values(
        first_name="Sus"
    )

    # Execute the statement within a session
    with Session() as session:
        session.execute(insert_stmt)
        session.commit()

        session.execute(update_stmt)
        session.commit()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
