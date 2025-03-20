from sqlalchemy import create_engine
from settings import settings

main_engine = create_engine(f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}")
