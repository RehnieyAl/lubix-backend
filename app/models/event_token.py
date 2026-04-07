from sqlalchemy import String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime, timedelta
from app.database.connection import Base
from enum import Enum as typerEnum

class TokenType(typerEnum):
    access = "access"
    refresh = "refresh"

class EventToken(Base):
    __tablename__ = "event_token"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )

    token: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    token_type: Mapped[TokenType] = mapped_column(
        Enum(TokenType), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow    
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.utcnow() + timedelta(minutes=15)
    )
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["Users"] = relationship(
        back_populates="EventToken"
    )