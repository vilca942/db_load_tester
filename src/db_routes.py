from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.database import get_db_session
import string
import random
from src.models import Sentence
from src.settings import settings

router = APIRouter()


def random_string() -> str:
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(settings.sentence_length))


@router.post("/write")
def write_to_db(
    sentence: str | None = None,
    db_session: Session = Depends(get_db_session),
) -> str:
    """writes a sentence to the database"""

    new_sentence = Sentence(sentence=sentence if sentence else random_string())

    db_session.add(new_sentence)
    db_session.commit()

    return "OK"


@router.get("/count_all")
def count_all(db_session: Session = Depends(get_db_session)) -> int:
    """counts all sentences from the database"""

    sentences = db_session.execute(select(Sentence)).all()

    return len(sentences)
