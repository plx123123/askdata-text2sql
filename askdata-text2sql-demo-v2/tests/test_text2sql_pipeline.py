from __future__ import annotations

from askdata_pipeline.objects import PipelineConfig
from askdata_pipeline.text2sql_pipeline import AskDataText2SQLPipeline


def test_text2sql_pipeline_runs_end_to_end_with_mock_models(tmp_path):
    pipeline = AskDataText2SQLPipeline(
        PipelineConfig(db_path=tmp_path / "trade_demo.db")
    )

    result = pipeline.run(
        query="Find interest_rate for users whose total_trade_count is greater than 50000",
        keywords=["total_trade_count", "interest_rate"],
    )

    assert result.keywords == ["total_trade_count", "interest_rate"]
    assert len(result.step_logs) == 1

    step_log = result.step_logs[0]

    assert "SELECT interest_info.interest_rate" in step_log.sql
    assert "JOIN interest_info" in step_log.sql
    assert step_log.execution_result["success"] is True
    assert step_log.execution_result["columns"] == ["interest_rate"]
    assert step_log.execution_result["row_count"] == 5
    assert step_log.execution_result["rows"][0]["interest_rate"] == 4.58

