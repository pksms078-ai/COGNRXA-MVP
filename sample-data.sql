SQL
database/knowledge-model.md
Markdown
database/entities-table.sql
SQL
CREATE TABLE entities (

entity_id INTEGER PRIMARY KEY,

document_id INTEGER,

entity_name TEXT,

entity_type TEXT,

description TEXT,

confidence_score REAL,

created_at TIMESTAMP

);
