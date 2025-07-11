from typing import Type

from numpy import ndarray
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .models import Chat, Message

# This function takes session, id of message from telegram, text of message and chat id, It creates new message
# entity and validate

def ensure_chat_exists(session: Session, chat_id: int) -> bool:
    try:
        if not session.query(Chat).filter(Chat.id == chat_id).first():
            chat = Chat(id=chat_id)
            session.add(chat)
            session.commit()
            return True
        return False
    except SQLAlchemyError as e:
        session.rollback()
        raise e

# This function takes sesstion, id of message from telegram, text of message and chat id, It creates new message
# entity and validates data. As validation here is checking of chat entity existing and similarity check
# returns bool
def save_message(session: Session, message_id: int, embeddings, chat_id: int) -> bool:
    try:
        print(embeddings)
        ensure_chat_exists(session, chat_id)
        if not session.query(Message).filter(Message.id == message_id).first():
            msg = Message(id=message_id, embeddings=embeddings, chat_id=chat_id)
            session.add(msg)
            session.commit()
            return True
        return False
    except SQLAlchemyError as e:
        session.rollback()
        raise e

# here function takes session and chat id, it returns list of message objects from database
def get_all_messages_by_chat(session: Session, chat_id: int):
    try:
        return session.query(Message).filter(Message.chat_id == chat_id).all()
    except SQLAlchemyError as e:
        session.rollback()
        raise e