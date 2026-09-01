from __future__ import annotations

from sql_generation import CoderModelClient, CoderModelConfig, CotStep, LocalSchemaStore
from sql_generation.sql_generator import SqlGenerator


def test_sql_generator_builds_join_query_from_local_schema():
    schema_store = LocalSchemaStore.build_demo_store()
    generator = SqlGenerator(
        schema_store=schema_store,
        coder_client=CoderModelClient(
            CoderModelConfig(use_mock_when_no_api_key=True)
        ),
    )

    result = generator.generate(
        CotStep(
            database="trade_db",
            processing_objects=(
                "trade_summary.total_trade_count, "
                "interest_info.interest_rate, "
                "trade_summary.user_id, "
                "interest_info.user_id"
            ),
            operation_instruction=(
                "Filter trade_summary.total_trade_count greater than 50000 "
                "and join interest_info by user_id."
            ),
            output_target="interest_info.interest_rate",
        )
    )

    assert result.database == "trade_db"
    assert result.sql.startswith("SELECT")
    assert "JOIN interest_info" in result.sql
    assert "trade_summary.total_trade_count > 50000" in result.sql
    assert result.to_execution_request() == {
        "database": "trade_db",
        "sql": result.sql,
    }

