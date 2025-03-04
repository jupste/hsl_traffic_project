CREATE TABLE alerts (
    id TEXT PRIMARY KEY,              -- Unique identifier for each alert
    alertheadertext TEXT NOT NULL,  -- Short title or summary of the alert
    alertdescriptiontext TEXT,      -- Full description of the alert
    alerturl TEXT,                   -- Optional URL with more details
    effectivestartdate INTEGER,   -- When the alert starts
    effectiveenddate INTEGER      -- When the alert ends
);

CREATE TABLE stops (
    id TEXT PRIMARY KEY,    -- Unique identifier for each stop
    gtfsid TEXT NOT NULL,   -- General Transit Feed Specification id for each stop
    name TEXT NOT NULL,     -- Name for each stop
    lat DOUBLE PRECISION,   -- Latitude for each stop
    lon DOUBLE PRECISION,   -- Longitude for each stop
    zoneid TEXT,            --
);

CREATE TABLE alerts_entities (
    __typename TEXT NOT NULL,
    gtfsid TEXT,
    alertId TEXT NOT NULL,
    PRIMARY KEY (__typename, gtfsid, alertId)
)