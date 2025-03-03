# Python 3.9 이미지를 기반으로 설정
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일들을 복사
COPY requirements.txt ./

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# (4) 현재 디렉터리(app 폴더)의 모든 내용(코드, 폴더)을 컨테이너 /app 에 복사
COPY . .

# 포트 설정 (FastAPI 기본 포트: 8000)
EXPOSE 3000

# 애플리케이션 실행
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]