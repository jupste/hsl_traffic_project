CREATE TABLE alerts (
    id TEXT PRIMARY KEY,              -- Unique identifier for each alert
    alert_header_text TEXT NOT NULL,  -- Short title or summary of the alert
    alert_description_text TEXT,      -- Full description of the alert
    alert_url TEXT,                   -- Optional URL with more details
    effective_start_date TIMESTAMP,   -- When the alert starts
    effective_end_date TIMESTAMP      -- When the alert ends
);


