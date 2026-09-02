from __future__ import annotations

from askdata_pipeline.objects import PipelineConfig
from askdata_pipeline.text2sql_pipeline import AskDataText2SQLPipeline


def test_schema_retrieval_keeps_metric_output_and_join_columns(tmp_path):
    pipeline = AskDataText2SQLPipeline(
        PipelineConfig(db_path=tmp_path / "trade_demo.db")
    )

    result = pipeline.schema_retrieval_service.retrieve(
        query="Find interest_rate for users whose total_trade_count is greater than 50000",
        keywords=["total_trade_count", "interest_rate"],
    )

    doc_ids = {hit.doc_id for hit in result.schema_hits}
    prompt_context = result.schema_graph.to_prompt_context()

    assert any(doc_id.endswith("trade_summary.total_trade_count") for doc_id in doc_ids)
    assert any(doc_id.endswith("interest_info.interest_rate") for doc_id in doc_ids)
    assert "trade_summary" in prompt_context
    assert "interest_info" in prompt_context
    assert "user_id" in prompt_context
