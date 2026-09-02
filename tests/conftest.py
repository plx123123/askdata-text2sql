from __future__ import annotations

import pytest


@pytest.fixture(autouse=True)
def force_local_mock_models(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep tests offline and deterministic."""
    monkeypatch.delenv("DASHSCOPE_API_KEY", raising=False)
    monkeypatch.delenv("DASHSCOPE_WORKSPACE_ID", raising=False)

