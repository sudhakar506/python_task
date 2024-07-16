import pytest
from app import Task

def test_get_response():
  actual_result = Task().get_response()
  assert actual_result == 200
