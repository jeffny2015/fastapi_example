from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from schema.pydantic_query import Query
import datetime



async def raw_query(db: AsyncSession, q: Query):
    statement = text(q.query)
    result = await db.execute(statement=statement)
    data = []
    if result.returns_rows:
        keys = result.keys()
        for r in result:
            parse_datetime = list(map(lambda x: x.isoformat() if isinstance(x, datetime.datetime) else x, r))
            d = dict(zip(keys, parse_datetime))
            data.append(d)
        return data
      
    rows = result.rowcount
    data = { "data" : f"Rows {rows} affected"}
    return data

