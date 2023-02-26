from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, Depends
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from config import db_settings



ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_settings.DB_USER}:{db_settings.DB_PASSWORD}@localhost:15432/{db_settings.DB_NAME}"


async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)

AsyncSessionLocal = sessionmaker(
    async_engine, class_= AsyncSession, expire_on_commit=False
)


Base = declarative_base()

async def async_get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
            await db.commit()
        except SQLAlchemyError as sql_exc:
            await db.rollback()
            # sql_exc
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
            )
        except HTTPException as http_exc:
            await db.rollback()
            #raise http_exc
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
            )
        finally:
                await db.close()