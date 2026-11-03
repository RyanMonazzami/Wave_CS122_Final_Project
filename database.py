from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Build engine
engine = create_engine('sqlite:///wave.db')

# Construct base class
Base = declarative_base()

# Create sessionmaker
Session = sessionmaker(bind=engine)

# Create all tables in database
def init_db():
    Base.metadata.create_all(engine)
