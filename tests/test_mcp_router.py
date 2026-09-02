from __future__ import annotations

from askdata_pipeline.data import create_trade_demo_database
from mcp_router.objects import MCPExecutionRequest
from mcp_router.sqlite_executor import SQLiteMCPExecutor


def test_sqlite_mcp_executor_runs_readonly_select(tmp_path):
    db_path = create_trade_demo_database(tmp_path / "trade.db")
    executor = SQLiteMCPExecutor(
        database="trade_db",
        db_path=db_path,
        readonly=True,
    )

    result = executor.execute(
        MCPExecutionRequest(
            database="trade_db",
            sql="SELECT COUNT(*) AS total FROM trade_summary;",
        )
    )

    assert result.success is True
    assert result.columns == ["total"]
    assert result.rows[0]["total"] > 0


def test_sqlite_mcp_executor_rejects_write_sql_in_readonly_mode(tmp_path):
    db_path = create_trade_demo_database(tmp_path / "trade.db")
    executor = SQLiteMCPExecutor(
        database="trade_db",
        db_path=db_path,
        readonly=True,
    )

    result = executor.execute(
        MCPExecutionRequest(
            database="trade_db",
            sql="UPDATE trade_summary SET total_trade_count = 0;",
        )
    )

    assert result.success is False
    assert result.error

