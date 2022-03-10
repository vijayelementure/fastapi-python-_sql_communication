from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base


connection_url = "sqlite:///./sql_app.db"

starting_point = create_engine(connection_url)

start_session = sessionmaker(starting_point)

base = declarative_base()