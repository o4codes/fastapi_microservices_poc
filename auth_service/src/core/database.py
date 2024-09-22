from sqlmodel import create_engine, Session
from src.core.config import config

ENGINE = None

def get_engine():
    global ENGINE
    if ENGINE is None:
        engine_kwargs = {"url": config.debug, "echo": config.debug}
        ENGINE = create_engine(**engine_kwargs)
    return ENGINE

def get_session():
    engine = get_engine()
    with Session(engine) as session:
        yield session
    