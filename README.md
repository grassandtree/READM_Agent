# README_Agent: AI 기반 README 자동 생성 및 업데이트 시스템

## 프로젝트 소개

`README_Agent`는 AI 에이전트 기반으로 GitHub 리포지토리의 README 문서를 자동으로 생성하고 업데이트하는 시스템입니다. 이 프로젝트는 개발자가 수동으로 README를 작성하는 시간과 노력을 절감하고, 항상 최신 상태의 정확한 프로젝트 문서를 유지할 수 있도록 지원합니다. GitHub API를 통해 리포지토리 정보를 분석하고, Google Gemini API를 활용한 LLM(Large Language Model) 에이전트들의 협업을 통해 프로젝트의 핵심 요소를 파악하여 체계적인 README를 자동으로 생성합니다.

*   **프로젝트명**: README_Agent
*   **저장소 URL**: https://github.com/grassandtree/README_Agent
*   **한 줄 요약**: AI 에이전트 기반의 GitHub README 자동 생성 및 업데이트 시스템

## 주요 기능

*   **AI 에이전트 기반 자동화**: `RepoManager`, `Analyst`, `TechExpert`, `Writer` 등 역할이 명확히 분리된 에이전트들이 협업하여 README 문서 생성 프로세스를 완전 자동화합니다.
*   **GitHub 리포지토리 연동**: GitHub API(PyGithub)를 사용하여 대상 리포지토리의 파일 트리 및 파일 내용을 추출하고, 최종적으로 생성된 README를 Pull Request로 발행합니다.
*   **지능형 프로젝트 분석**: Google Gemini API를 활용하여 LLM이 프로젝트 코드, 구조 및 기술 스택을 심층적으로 분석하고 요약합니다.
*   **동적 핵심 파일 선택**: LLM을 통해 프로젝트의 특성에 따라 README 생성에 필요한 핵심 파일을 동적으로 선별합니다.
*   **구조화된 README 생성**: 분석된 데이터를 바탕으로 프로젝트 소개, 주요 기능, 기술 스택, 아키텍처 등 표준화된 섹션을 포함하는 README.md 마크다운을 생성합니다.
*   **환경 변수 기반 설정**: `python-dotenv`를 통해 민감 정보(예: API 키) 및 환경 설정을 안전하게 관리합니다.

## 프로젝트 구조

자세한 디렉토리 구조는 제공되지 않았습니다. 하지만 아키텍처 분석을 통해 시스템의 주요 구성 요소를 추정할 수 있습니다.

*   `main.py`: 시스템의 진입점 및 에이전트 오케스트레이션을 담당하는 핵심 스크립트.
*   `.env`: 환경 변수 관리를 위한 파일. GitHub 토큰, Gemini API 키 등 민감 정보가 포함될 것으로 추정됩니다.
*   에이전트 모듈 (추정): 각 에이전트(`RepoManagerAgent`, `AnalystAgent`, `TechExpertAgent`, `WriterAgent`)는 별도의 Python 모듈로 구현되어 역할을 분담할 것으로 추정됩니다.
*   생성된 README 파일: `README.md` (로컬에 임시 저장되거나, 직접 GitHub에 발행됩니다.)

## 핵심 파일 설명

*   **`main.py`**:
    이 프로젝트의 핵심 진입점으로, 시스템 전체의 흐름을 제어합니다. 환경 변수를 로드하고, `RepoManagerAgent`, `AnalystAgent`, `TechExpertAgent`, `WriterAgent`와 같은 각 에이전트를 초기화하며, 이들 에이전트 간의 작업을 조율하여 README 생성 프로세스를 시작하고 완료합니다. 최종적으로 생성된 README를 GitHub에 Pull Request로 발행하는 역할까지 총괄합니다.

## 기술 스택

이 프로젝트는 다음과 같은 기술 스택을 활용하여 개발되었습니다.

*   **Backend**:
    *   **Python**: 다재다능하고 읽기 쉬운 언어로, 빠른 개발과 다양한 라이브러리 활용에 유리하여 프로젝트 구현 시간을 단축하고 복잡한 로직을 명확하게 표현할 수 있습니다.
    *   **Agent-based Architecture**: 역할을 분리하고 독립적으로 기능을 수행하는 에이전트들을 통해 복잡한 작업을 모듈화하고 관리하기 용이하여 시스템의 확장성과 유지보수성을 높입니다.
    *   **python-dotenv**: 환경 변수를 안전하게 관리하여 민감 정보를 코드에서 분리하고, 개발 및 배포 환경 설정의 유연성을 확보하여 보안성과 이식성을 높입니다.
*   **AI/Generative AI**:
    *   **Google Gemini API (google-generativeai)**: 강력한 최신 대규모 언어 모델을 활용하여 복잡한 텍스트 분석, 요약, 생성 작업을 효과적으로 수행하며, AI 기반 기능을 시스템에 손쉽게 통합하여 지능적인 자동화 기능을 제공합니다.
*   **External Integration**:
    *   **GitHub API (PyGithub)**: GitHub 리포지토리의 파일 구조, 내용 추출 및 Pull Request 생성과 같은 핵심 기능을 프로그래밍 방식으로 제어하여, 자동화된 워크플로우를 구축하고 개발 생산성을 크게 향상시킵니다.
*   **Utilities**:
    *   **JSON**: 데이터 교환 및 저장을 위한 표준 형식으로, 에이전트 간의 정보 전달과 AI 모델의 구조화된 응답 처리를 용이하게 하여 시스템의 데이터 처리 효율성과 상호운용성을 높입니다.

## 시스템 아키텍처

이 시스템은 GitHub 리포지토리의 README 문서를 자동으로 생성하고 업데이트하기 위한 에이전트 기반의 워크플로우 자동화 도구입니다. `main.py`를 중심으로 여러 에이전트(`RepoManager`, `Analyst`, `TechExpert`, `Writer`)가 순차적으로 협업하며 작업을 수행합니다.

1.  **사용자 시작**: `main.py` 스크립트가 실행되면 환경 변수를 로드하고 각 에이전트를 초기화합니다.
2.  **리포지토리 데이터 추출 (`RepoManagerAgent`)**: `RepoManagerAgent`는 GitHub API를 통해 대상 리포지토리의 파일 트리를 추출합니다. LLM(Gemini API)을 활용하여 이 파일 트리에서 README 생성에 필요한 핵심 파일을 선별하고, 해당 파일의 내용을 가져옵니다.
3.  **프로젝트 분석 (`AnalystAgent`)**: `AnalystAgent`는 `RepoManagerAgent`로부터 전달받은 핵심 파일 내용을 바탕으로 프로젝트의 구조와 기능을 심층적으로 분석합니다. 이 과정에서도 Gemini API를 활용하여 지능적인 분석을 수행합니다.
4.  **기술 스택/아키텍처 분석 (`TechExpertAgent`)**: `TechExpertAgent`는 `AnalystAgent`의 분석 결과를 이어받아 프로젝트의 기술 스택 및 시스템 아키텍처를 상세하게 분석하고 요약합니다. 이 또한 Gemini API를 통해 이루어집니다.
5.  **README 초안 작성 (`WriterAgent`)**: `WriterAgent`는 이전 단계에서 수집되고 분석된 모든 데이터를 통합하여 최종 README 마크다운 문서를 생성합니다. 생성된 README는 로컬에 저장되며, 다음 단계로 전달됩니다.
6.  **Pull Request 생성 (`RepoManagerAgent`)**: 최종적으로 생성된 README 마크다운은 다시 `RepoManagerAgent`로 전달되어, GitHub API를 통해 대상 리포지토리에 새로운 브랜치 생성 및 Pull Request로 발행됩니다.

모든 에이전트는 Google Gemini API를 활용하여 지능적인 분석 및 생성 작업을 수행함으로써 시스템의 자동화 수준을 극대화합니다.

```mermaid
graph TD
    classDef backend fill:#D4E6F1,stroke:#3498DB,stroke-width:2px;
    classDef external fill:#FADBD8,stroke:#E74C3C,stroke-width:2px;
    classDef storage fill:#D1F2EB,stroke:#2ECC71,stroke-width:2px;
    classDef user fill:#FCF3CF,stroke:#F1C40F,stroke-width:2px;

    User["사용자"]:::user --> main_py["main.py"]:::backend;
    
    subgraph "README 생성 시스템"
        main_py -- "1. 환경 변수 로드" --> ENV["`.env` 환경변수"]:::storage;
        main_py -- "2. 에이전트 초기화" --> RepoManagerAgent["RepoManagerAgent"]:::backend;
        main_py -- "2. 에이전트 초기화" --> AnalystAgent["AnalystAgent"]:::backend;
        main_py -- "2. 에이전트 초기화" --> TechExpertAgent["TechExpertAgent"]:::backend;
        main_py -- "2. 에이전트 초기화" --> WriterAgent["WriterAgent"]:::backend;

        RepoManagerAgent -- "Step 1: 대상 리포지토리 데이터 추출" --> GithubAPI["GitHub API"]:::external;
        GithubAPI -- "파일 트리, 핵심 파일 내용" --> RepoManagerAgent;
        RepoManagerAgent -- "LLM 파일 선택" --> GeminiAPI["Gemini API"]:::external;
        GeminiAPI -- "선택된 파일 목록 (JSON)" --> RepoManagerAgent;
        RepoManagerAgent -- "프로젝트 데이터" --> AnalystAgent;
        
        AnalystAgent -- "Step 2: 프로젝트 분석 요청" --> GeminiAPI;
        GeminiAPI -- "분석 결과 (JSON)" --> AnalystAgent;
        AnalystAgent -- "분석 요약" --> TechExpertAgent;
        
        TechExpertAgent -- "Step 3: 기술 스택 분석 요청" --> GeminiAPI;
        GeminiAPI -- "기술 스택/아키텍처 (JSON)" --> TechExpertAgent;
        TechExpertAgent -- "기술 스택 요약" --> WriterAgent;
        
        WriterAgent -- "Step 4: README 초안 작성 요청" --> GeminiAPI;
        GeminiAPI -- "README 마크다운" --> WriterAgent;
        WriterAgent -- "README.md" --> LocalFile["로컬 `README.md` 저장"]:::storage;
        WriterAgent -- "README 마크다운" --> RepoManagerAgent;
        
        RepoManagerAgent -- "Step 5: PR 생성" --> GithubAPI;
        GithubAPI -- "PR URL" --> main_py;
    end
    
    GithubAPI -- "대상 GitHub Repository" --> TargetRepo["grassandtree/READM_Agent 또는 `TARGET_REPO`"]:::external;
    TargetRepo -- "파일 변경, PR" --> GithubAPI;
```

## 실행 방법

실행 방법은 추가 작성 필요합니다.

## 기술 선택 이유

이 프로젝트의 기술 스택은 다음과 같은 이유로 선택되었습니다.

*   **Python**: 다재다능하고 읽기 쉬운 언어로, 빠른 개발과 다양한 라이브러리 활용에 유리하여 프로젝트 구현 시간을 단축하고 복잡한 로직을 명확하게 표현할 수 있습니다.
*   **Agent-based Architecture**: 역할을 분리하고 독립적으로 기능을 수행하는 에이전트들을 통해 복잡한 작업을 모듈화하고 관리하기 용이하며, 시스템의 확장성과 유지보수성을 높입니다.
*   **python-dotenv**: 환경 변수를 안전하게 관리하여 민감 정보를 코드에서 분리하고, 개발 및 배포 환경 설정의 유연성을 확보하여 보안성과 이식성을 높입니다.
*   **Google Gemini API**: 강력한 최신 대규모 언어 모델을 활용하여 복잡한 텍스트 분석, 요약, 생성 작업을 효과적으로 수행하고, AI 기반 기능을 시스템에 통합하여 지능적인 자동화 기능을 제공합니다.
*   **GitHub API (PyGithub)**: GitHub 리포지토리의 파일 구조, 내용 추출 및 Pull Request 생성과 같은 핵심 기능을 프로그래밍 방식으로 제어하여 자동화된 워크플로우를 구축하고 개발 생산성을 크게 향상시킵니다.
*   **JSON**: 데이터 교환 및 저장을 위한 표준 형식으로, 에이전트 간의 정보 전달과 AI 모델의 구조화된 응답 처리를 용이하게 하여 시스템의 데이터 처리 효율성과 상호운용성을 높입니다.

## 개선 방향

현재 프로젝트는 강력한 자동화 기능을 제공하지만, 다음과 같은 방향으로 추가 개선을 고려할 수 있습니다.

*   **README 내용 품질 및 정확도 향상**:
    *   사용자 피드백 루프를 구현하여 생성된 README에 대한 검토 및 수정을 시스템이 학습하고 반영하도록 개선.
    *   다양한 프로젝트 유형(예: 프런트엔드, 백엔드, 모바일 앱, 데이터 과학)에 특화된 분석 모델 및 프롬프트 개발.
*   **다양한 문서 형식 지원**:
    *   Markdown 외에 Confluence, Notion 등 다른 문서 플랫폼 형식으로 README를 내보낼 수 있는 기능 추가.
*   **템플릿 기반 README 생성**:
    *   사용자가 커스텀 템플릿을 정의하고 이를 기반으로 README를 생성할 수 있도록 하여 유연성 증대.
*   **성능 최적화 및 비용 효율성**:
    *   LLM 호출 횟수를 줄이기 위한 캐싱 메커니즘 도입 또는 더 효율적인 프롬프트 엔지니어링 기법 적용.
    *   비용 효율적인 LLM 모델 선택 옵션 제공.
*   **CI/CD 파이프라인 통합**:
    *   GitHub Actions 등의 CI/CD 도구와 연동하여 코드 변경 시 자동으로 README를 업데이트하도록 설정.
*   **에러 처리 및 로깅 강화**:
    *   GitHub API 호출 실패 또는 LLM 응답 오류 시 명확한 에러 메시지와 재시도 로직 구현.
    *   자세한 로깅 시스템을 구축하여 문제 발생 시 디버깅 용이성 확보.
*   **보안 강화**:
    *   API 토큰 및 민감 정보 관리에 대한 추가적인 보안 검토 및 모범 사례 적용.