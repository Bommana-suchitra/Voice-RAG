# ===================================================================================
# Project: VoiceRAG
# File: src/db/factory.py
# Description: Async connection with PostgresDB
# Author: LALAN KUMAR
# Created: [04-03-2026]
# Updated: [04-03-2026]
# LAST MODIFIED BY: LALAN KUMAR  [https://github.com/kumar8074]
# Version: 1.0.0
# ===================================================================================

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from ..config import (POSTGRES_HOST, POSTGRES_USER, POSTGRES_PASSWORD, 
                      POSTGRES_PORT, POSTGRES_DB)

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)

engine_kwargs = {"echo": False}
if "sqlite" not in DATABASE_URL:
    engine_kwargs.update({
        "pool_pre_ping": True,
        "pool_size": 10,
        "max_overflow": 20
    })

engine = create_async_engine(
    DATABASE_URL,
    **engine_kwargs
)

async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)