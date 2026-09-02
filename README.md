# AskData Text2SQL Demo

面向业务人员的自然语言取数 Demo：从自然语言 Query 出发，经过 Schema 索引与混合检索、结构化查询计划、SQL 生成和只读工具执行，返回可验证的查询结果。

## 项目亮点

- 表级、字段级、指标级 Schema 组织
- 关键词检索与向量检索的混合召回
- RRF 融合与 Rerank 精排
- Schema Graph 辅助 Join 关系构建
- 查询规划、SQL 生成与 MCP Router 只读执行
- 本地 SQLite 演示库与 Mock 模型回退，开箱可运行

## 运行

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m askdata_pipeline.end_to_end_demo
```

运行测试：

```bash
pytest -q
```

## 当前链路

```text
自然语言 Query
  -> 关键词抽取
  -> Schema 混合检索
  -> RRF 融合与 Rerank
  -> Schema Graph
  -> 结构化查询计划
  -> SQL 生成
  -> MCP Router 只读执行
  -> 查询结果
```

## 公开版边界

- 示例数据仅用于本地演示，不连接真实业务数据库。
- 未提交 API Key、真实企业数据、虚拟环境和运行时数据库。
- 当前 Demo 重点覆盖检索、规划、生成和执行；结果校验与回溯修正属于后续扩展方向。
