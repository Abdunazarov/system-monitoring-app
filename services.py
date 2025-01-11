# stdlib
import psutil

# third-party
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# project
from models import SystemUsage

async def get_system_metrics():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu_usage": cpu_usage,
        "ram_free": memory.available / (1024 * 1024),
        "ram_total": memory.total / (1024 * 1024),
        "disk_free": disk.free / (1024 * 1024),
        "disk_total": disk.total / (1024 * 1024)
    }

async def record_system_usage(session: AsyncSession):
    metrics = await get_system_metrics()
    record = SystemUsage(
        cpu_usage=metrics["cpu_usage"],
        ram_free=metrics["ram_free"],
        ram_total=metrics["ram_total"],
        disk_free=metrics["disk_free"],
        disk_total=metrics["disk_total"]
    )
    session.add(record)
    await session.commit()

async def fetch_history(session: AsyncSession):
    query = select(SystemUsage).order_by(SystemUsage.timestamp.desc())
    result = await session.execute(query)
    return [{"timestamp": record.timestamp, "cpu_usage": record.cpu_usage} for record in result.scalars().all()]
