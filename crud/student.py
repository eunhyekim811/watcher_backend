from sqlmodel import Session, select
from app.models.snapshot import Snapshot
from fastapi import HTTPException
import numpy as np

def get_snapshot_data(db: Session, class_div:str, hw_name:str, student_id:int, filename:str):
    # 데이터베이스에서 해당 스냅샷 조회(select문)
    statement = select(Snapshot).where(
        Snapshot.class_div == class_div, 
        Snapshot.hw_name == hw_name, 
        Snapshot.student_id == student_id, 
        Snapshot.filename == filename
    )
    
    results = db.exec(statement).all()
    return results
    
    