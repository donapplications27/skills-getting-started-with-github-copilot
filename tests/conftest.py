import copy
import pytest
from fastapi.testclient import TestClient
import src.app as app_module


@pytest.fixture
def client():
    with TestClient(app_module.app) as c:
        yield c


@pytest.fixture(autouse=True)
def isolate_activities():
    """Deep-copy and restore the in-memory activities mapping for each test."""
    original = copy.deepcopy(app_module.activities)
    try:
        yield
    finally:
        app_module.activities.clear()
        app_module.activities.update(original)
