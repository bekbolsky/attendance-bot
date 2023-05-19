from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config_data.config import DB_URL
from database.models import Base


engine = create_engine(DB_URL)
Session = sessionmaker(autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)
