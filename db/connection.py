from sqlmodel import create_engine, SQLModel, Session
from typing import Annotated
from fastapi import Depends
from app.models.snapshot import Snapshot
from dotenv import load_dotenv

load_dotenv()

# 해당 경로에 db 파일 없는 경우 자동 생성
sqlite_file_name = "database.db"   # sqlite db 파일 이름
# sqlite_url = f"sqlite:////home/ubuntu/backend/app/db/{sqlite_file_name}"   # sqlite db 파일 경로
sqlite_url = f"sqlite:///app/db/{sqlite_file_name}"

connect_args = {"check_same_thread": False}   # fastapi에서 여러 스레드에서 동일한 sqlite db 사용 가능  
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
# echo=True : 모든 sql 문장 출력

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def insert_data():
    with Session(engine) as session:
        snapshots = [
            Snapshot(class_div="os-1", hw_name="hw2", student_id=202511111, filename="aaaa.c", timestamp="20250226_082535", file_size=52),
            Snapshot(class_div="os-1", hw_name="hw2", student_id=202522222, filename="bbbb.c", timestamp="20250226_082804", file_size=3),
            Snapshot(class_div="os-1", hw_name="hw2", student_id=202533333, filename="cccc.c", timestamp="20250226_082900", file_size=42),
            Snapshot(class_div="os-1", hw_name="hw2", student_id=202544444, filename="dddd.c", timestamp="20250226_083000", file_size=99),
            Snapshot(class_div="os-1", hw_name="hw2", student_id=202555555, filename="eeee.c", timestamp="20250224_083100", file_size=33),
            Snapshot(class_div="os-1", hw_name="hw2", student_id=202566666, filename="ffff.c", timestamp="20250224_083200", file_size=18),
            Snapshot(class_div="os-1", hw_name="hw1", student_id=202577777, filename="gggg.c", timestamp="20250224_083300", file_size=9),
            Snapshot(class_div="os-1", hw_name="hw1", student_id=202588888, filename="hhhh.c", timestamp="20250224_083400", file_size=46),
            Snapshot(class_div="os-1", hw_name="hw1", student_id=202599999, filename="iiii.c", timestamp="20250224_083500", file_size=28),
            
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250220_082535", file_size=2),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250220_082804", file_size=15),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250223_082900", file_size=50),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250223_083000", file_size=42),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250223_083100", file_size=67),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250223_083200", file_size=89),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250225_083300", file_size=75),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250225_083400", file_size=80),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250226_083500", file_size=93),
            # Snapshot(class_div="os-1", hw_name="hw2", student_id=202212112, filename="example.c", timestamp="20250226_083600", file_size=100)
        ]
        
        session.add_all(snapshots)
        session.commit()
    
def get_session():
    with Session(engine) as session:
        yield session

# SessionDep = Annotated[Session, Depends(get_session)]