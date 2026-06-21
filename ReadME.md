Markdown
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    organization TEXT,
    created_at TIMESTAMP
);

CREATE TABLE documents (
    document_id INTEGER PRIMARY KEY,
    title TEXT,
    document_type TEXT,
    source TEXT,
    upload_date TIMESTAMP,
    content TEXT
);

CREATE TABLE entities (
    entity_id INTEGER PRIMARY KEY,
    document_id INTEGER,
    entity_name TEXT,
    entity_type TEXT
);

CREATE TABLE patterns (
    pattern_id INTEGER PRIMARY KEY,
    pattern_name TEXT,
    confidence_score REAL,
    discovered_date TIMESTAMP
);

CREATE TABLE insights (
    insight_id INTEGER PRIMARY KEY,
    insight_title TEXT,
    description TEXT,
    generated_date TIMESTAMP
);

CREATE TABLE decisions (
    decision_id INTEGER PRIMARY KEY,
    recommendation TEXT,
    risk_level TEXT,
    generated_date TIMESTAMP
);
