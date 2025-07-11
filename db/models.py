from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import ARRAY, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Chat(Base):
    __tablename__ = 'Chat'

    id = Column('ID', Integer, primary_key=True)
    messages = relationship("Message", back_populates="chat")


class Message(Base):
    __tablename__ = 'Messages'

    id = Column('ID', Integer, primary_key=True)
    embeddings = Column(JSON)
    chat_id = Column('Chat_ID', Integer, ForeignKey('Chat.ID'))

    chat = relationship("Chat", back_populates="messages")
