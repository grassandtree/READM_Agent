"""
Constants used across the README_Agent project.
"""

REQUIRED_README_SECTIONS = [
    "프로젝트 소개",
    "주요 기능",
    "프로젝트 구조",
    "핵심 파일 설명",
    "기술 스택",
    "시스템 아키텍처",
    "실행 방법",
    "기술 선택 이유",
    "개선 방향"
]

MODE_TONES = {
    "portfolio": "면접과 포트폴리오 제출에 적합한 README로 작성하세요.",
    "beginner": "초보 개발자가 읽어도 이해하기 쉽게 설명하세요.",
    "professional": "오픈소스 프로젝트 문서처럼 정돈된 형식으로 작성하세요.",
}

JSON_OUTPUT_INSTRUCTION = "반드시 아래 JSON 형식으로만 응답해:"

MERMAID_CLASSDEF_RULES = """   - 반드시 'graph TD' 형식을 사용해.
   - 아래의 색상 클래스 정의를 다이어그램 맨 위에 반드시 포함해:
     classDef backend fill:#D4E6F1,stroke:#3498DB,stroke-width:2px;
     classDef external fill:#FADBD8,stroke:#E74C3C,stroke-width:2px;
     classDef storage fill:#D1F2EB,stroke:#2ECC71,stroke-width:2px;
     classDef user fill:#FCF3CF,stroke:#F1C40F,stroke-width:2px;
   - 문법 오류 방지 규칙:
     * 화살표 위의 텍스트는 반드시 큰따옴표로 감싸 (예: -- "데이터 전송" -->).
     * 노드 이름이나 설명에 공백, 특수문자(., #, / 등)가 있다면 반드시 큰따옴표나 대괄호로 감싸 (예: main_py["main.py"]:::backend).
     * 명령어 끝에 세미콜론(;)을 절대 붙이지 마."""