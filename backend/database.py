import sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).resolve().parent.parent / "privacy_assessment.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS assessments (
        assessment_id TEXT PRIMARY KEY,
        overall_score INTEGER NOT NULL,
        risk_level TEXT NOT NULL,
        created_at TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS category_scores (
        category_score_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_id TEXT NOT NULL,
        category TEXT NOT NULL,
        score INTEGER NOT NULL,
        FOREIGN KEY(assessment_id) REFERENCES assessments(assessment_id)
    );
    CREATE TABLE IF NOT EXISTS findings (
        finding_id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_id TEXT NOT NULL,
        category TEXT NOT NULL,
        finding_type TEXT NOT NULL,
        severity TEXT NOT NULL,
        description TEXT NOT NULL,
        FOREIGN KEY(assessment_id) REFERENCES assessments(assessment_id)
    );
    CREATE TABLE IF NOT EXISTS recommendations (
        recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        finding_type TEXT NOT NULL,
        recommendation TEXT NOT NULL,
        priority TEXT NOT NULL
    );
    """)
    conn.commit()
    conn.close()

def save_assessment(assessment_id, result, findings):
    conn = get_conn()
    created_at = datetime.now(timezone.utc).isoformat()
    conn.execute("INSERT INTO assessments VALUES (?,?,?,?)",
                 (assessment_id, result["overall_score"], result["risk_level"], created_at))
    for category, score in result["category_scores"].items():
        conn.execute("INSERT INTO category_scores (assessment_id,category,score) VALUES (?,?,?)",
                     (assessment_id, category, score))
    for f in findings:
        conn.execute("""INSERT INTO findings
            (assessment_id,category,finding_type,severity,description)
            VALUES (?,?,?,?,?)""",
            (assessment_id,f["category"],f["finding_type"],f["severity"],f["description"]))
    conn.commit()
    conn.close()
    return created_at

def get_assessment(assessment_id):
    conn = get_conn()
    a = conn.execute("SELECT * FROM assessments WHERE assessment_id=?", (assessment_id,)).fetchone()
    if not a:
        conn.close()
        return None
    cats = conn.execute("SELECT category,score FROM category_scores WHERE assessment_id=?", (assessment_id,)).fetchall()
    finds = conn.execute("SELECT category,finding_type,severity,description FROM findings WHERE assessment_id=?", (assessment_id,)).fetchall()
    conn.close()
    return {
        "assessment_id": a["assessment_id"], "overall_score": a["overall_score"],
        "risk_level": a["risk_level"], "created_at": a["created_at"],
        "category_scores": {r["category"]: r["score"] for r in cats},
        "findings": [dict(r) for r in finds],
    }

def dashboard_stats():
    conn = get_conn()
    total = conn.execute("SELECT COUNT(*) c FROM assessments").fetchone()["c"]
    distribution = {level: conn.execute("SELECT COUNT(*) c FROM assessments WHERE risk_level=?", (level,)).fetchone()["c"]
                    for level in ["LOW","MODERATE","HIGH","CRITICAL"]}
    avg = conn.execute("SELECT COALESCE(AVG(overall_score),0) a FROM assessments").fetchone()["a"]
    conn.close()
    return {"total_assessments": total, "average_score": round(avg,1), "risk_distribution": distribution}
