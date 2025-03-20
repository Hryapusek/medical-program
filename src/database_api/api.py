from sqlalchemy import create_engine

main_engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
