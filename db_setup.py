from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
import asyncio

DATABASE_URL = "postgresql+asyncpg://monitor_user:password@localhost/monitoring"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def check_db_connection():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        print("✅ Database is reachable.")
    except OperationalError:
        print("❌ Database connection failed. Ensure PostgreSQL is running.")
        exit(1)

if __name__ == "__main__":
    asyncio.run(check_db_connection())
    asyncio.run(init_db())
