import os
import traceback

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from db.repository import save_message, get_all_messages_by_chat

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
from sklearn.metrics.pairwise import cosine_similarity
from numpy import argmax


# It is a service that establish local database
class Database:
    def __init__(self) -> None:
        # DB setup
        engine = create_engine("sqlite:///chat.db")
        if not os.path.exists("chat.db"):
            Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    # Creating session
    def create_session(self):
        session = self.Session()
        return session

    # Closing session
    def close_session(self, session):
        session.close()

    # Saving message in database
    def save_message(self, message_id, text, chat_id):
        session = db.create_session()
        try:
            embedding = model.encode([text, ]).tolist()
            save_message(session, message_id, embedding, chat_id)
        except Exception as e:
            error = traceback.format_exc()
            print(f"Message save error: {error}")

        finally:
            session.close()

    # Showing all messages in database as a list of messages model
    def get_best_fit(self, context, chat_id):

        session = db.create_session()
        try:
            messages = get_all_messages_by_chat(session, chat_id)
        finally:
            db.close_session(session)

        # create tmp classes save the best fit one and return id of a chat

        repo_list = []

        for message in messages:
            repo_list.append(message.embeddings[0])

        embedding = model.encode([context, ])

        similirities = cosine_similarity(embedding, repo_list)

        max_id = argmax(similirities[0])

        return messages[max_id].id


db = Database()
