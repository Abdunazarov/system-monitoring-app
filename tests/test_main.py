from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from main import app
import pytest

client = TestClient(app)

@pytest.mark.asyncio
@patch("main.get_system_metrics", new_callable=AsyncMock)
async def test_get_metrics(mock_get_system_metrics):
    """Test the /metrics endpoint."""
    
    mock_get_system_metrics.return_value = {
        "cpu_usage": 35.5,
        "ram_free": 2048,
        "ram_total": 8192,
        "disk_free": 50000,
        "disk_total": 100000
    }

    response = client.get("/metrics")

    assert response.status_code == 200
    assert response.json() == mock_get_system_metrics.return_value
    mock_get_system_metrics.assert_called_once()


@pytest.mark.asyncio
@patch("main.record_system_usage", new_callable=AsyncMock)
async def test_start_recording(mock_record_system_usage, mock_db_session):
    """Test the /start-recording endpoint."""
    
    mock_record_system_usage.return_value = None

    response = client.post("/start-recording")

    assert response.status_code == 200
    assert response.json() == {"message": "Recording started"}
    mock_record_system_usage.assert_called_once_with(mock_db_session)


@pytest.mark.asyncio
@patch("main.fetch_history", new_callable=AsyncMock)
async def test_get_history(mock_fetch_history, mock_db_session):
    """Test the /history endpoint."""
    
    mock_fetch_history.return_value = [
        {
            "cpu_usage": 40.1,
            "ram_free": 1024,
            "ram_total": 8192,
            "disk_free": 45000,
            "disk_total": 100000
        }
    ]

    response = client.get("/history")

    assert response.status_code == 200
    assert response.json() == mock_fetch_history.return_value
    mock_fetch_history.assert_called_once_with(mock_db_session)
