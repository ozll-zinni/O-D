# Project Documentation

## 목차

1. [개요](#1-개요)
2. [협업 방법](#2-협업-방법)
3. [개발 환경 설정](#3-개발-환경-설정)
4. [코드 작성 규칙](#4-코드-작성-규칙)
5. [자주 발생하는 문제](#5-자주-발생하는-문제)
6. [참고 자료](#6-참고-자료)

## 1. 개요

- 일반적으로 개발을 진행할 때, README.md나 Confluence를 사용해서 협업을 위한 규칙을 문서화하고, 프로젝트의 API를 Swagger과 같은 도구를 사용해서 API 명세를 작성하는 걸로 알고 있어요. 그래서 저희의 협업을 위해서 README.md를 작성했습니다. 🙂

- 여러분이 얼마나 아는지를 몰라서 일단 최대한 자세하게 작성했습니다. 기분이 나쁘셨다면 미리 사과드릴게요. 😢

- `[본인의 이름].md` 파일을 만들어서 본인이 만들거나 수정한 코드에 대해서 기본적인 설명을 적어주세요. 다른 팀원들이 본인의 코드를 이해할 수 있도록 하면 좋을 것 같아요. 제가 주기적으로 확인하고, 각자의 `[본인의 이름].md`과 `README.md`를 병합하도록 할게요. 😊 [[참고1]](https://gist.github.com/ihoneymon/652be052a0727ad59601), [[참고2]](/Myeongkyu.md)

- `README.md`에 이런 내용이 추가되면 좋을 것 같다고 생각하는 부분이 있으면 말해주세요! 적극 반영하겠습니다. 🫡

## 2. 협업 방법

### Git 사용 규칙

- **Git 플로우**: release - git actions(CI/CD) - main(AWS 배포용 브랜치) - develop(개발용 브랜치) - feature branch(개인 브랜치) [[참고1]](https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html), [[참고2]](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

- 링크를 읽어보시면 알겠지만, 추후 개선을 버전 관리를 위한 release branch도 필요하고, feature branch는 보통 기능이 들어가야 하고 여러가지가 조금 달라요. 편의상 각자의 이름으로 해서 하면 좋을 것 같아서 이렇게 했습니다.

- 작업 시작 전 `git checkout [branch_name]`으로 본인의 branch로 이동해서 `git branch -v`로 본인의 branch로 이동되었는지 확인하고, `git merge develop`으로 branch와 develop 브랜치를 병합해서 동기화합니다. develop branch는 모든 조원의 작업들을 merge하기 때문에 계속해서 바뀌기 때문에 병합해서 동기화로 충돌을 최소화합니다. 충돌이 발생했을 때는 기본적으로 develop branch의 내용을 따르고, 본인의 branch를 develop branch에 병합을 해야한다고 생각될 경우에는 모두에게 알려주세요.

- 자신의 코드의 버전관리를 위해서 본인의 branch에 본인이 작업한 내용을 `git push origin [branch_name]`로 push합니다.

- **자신의 branch**에만 병합하도록 합니다. 특정 작업이 끝나면 repository에서 **본인의 branch**로 이동해서, pull request 버튼을 눌러서 develop branch에 병합을 요청합니다.
  ![pull request](/description_images/pull-request.png)

- 100MB 이상의 파일은 올리면 안 됩니다. git LFS(Large File Storage)를 사용해야하는데, 굳이 쓸 필요가 없다고 생각이 되네요. 따라서 해당 파일 형식은 .gitignore에 추가해야 합니다.

- 이번 프로젝트를 통해서 모두 git 이용 방법을 확실하게 익히고 가면 좋을 거라 생각합니다. 저도 협업이 처음이라서 기본적인 규칙만 정해봤는데, 추가적인 제안 사항이 있다면 말해주세요.

### 개인 branch 생성 및 사용 방법

1. 새로운 branch 생성 후 해당 브랜치로 이동

```bash
git checkout -b [branch_name]
```

2. 작업 후 모든 파일을 staging area로 이동시키기

```bash
git add .
```

3. staging area에 있는 파일들의 버전을 저장함

```
git commit -m "[commit_message]"
```

3. 처음에 자신의 branch에 push: upstream을 설정함

```bash
git push -u origin [branch_name]
```

4. 이후에 자신에 branch에 push: upstream이 설정되었으므로 -u 옵션은 불필요함

```bash
git push origin [branch_name]
```

## 3. 개발 환경 설정

### Postgresql 설치하기

- Postgresql를 설치합니다. [[참고1]](https://www.postgresql.org/download/), [[참고2]](https://medium.com/@heeee/django-django%EC%99%80-postgresql%EC%9D%80-%EC%99%9C-%EA%B6%81%ED%95%A9%EC%9D%B4-%EC%A2%8B%EC%9D%84%EA%B9%8C-1%ED%83%84-54af53bec906)

### 가상환경 사용해서 의존성 관리하기

1. 가상 환경을 생성할 경로로 이동하기

```bash
cd [path]
```

2. 가상 환경 생성

```bash
python -m venv [virtual_environment_name]
```

3. 가상 환경 활성화

```bash
[virtual_environment_path_name]\Scripts\activate
```

4. 해당 프로젝트 경로로 다시 이동하기

```bash
cd [path]
```

5. 필요한 패키지 설치하기

```bash
pip install -r requirements.txt
```

6. 현재 본인의 가상환경의 의존성을 프로젝트 환경으로 복사하기

```bash
pip freeze > requirements.txt
```

7. 가상환경 종료하기

```bash
deactivate
```

## 4. 코드 작성 규칙

### 언어별 가이드라인

#### python

- PEP 8 스타일 가이드를 준수합니다. [[참고]](https://ultrakain.gitbooks.io/python/content/chapter1/coding-style-pep8.html)

#### html/css

- Bootstrap의 class를 활용하고, 본인이 직접 `<style></style>`안에 css를 정의하는 일은 하지 않도록 합니다. 본인이 개별적으로 정의한 css로 인해서 팀원이 작성한 디자인이 망가지는 경우가 있을 수 있습니다.
- Chat GPT에게 물어볼 때 "Bootstrap5를 사용하고, 직접 style을 정의하지 않고 ㅇㅇ를 만들어줘"와 같은 식으로 부탁하면 좋아요.

#### JavaScript

- 최대한 Bootstrap의 컴포넌트를 활용합니다. [[참고]](https://getbootstrap.kr/docs/5.3/components/accordion/)
- 본인이 직접 효과를 넣고 싶다면 Jquery, React와 같은 프레임워크는 사용하지 않고, Vanilla Script로 작성하도록 합니다.
- 추후에 시간이 남으면(?), React로 리팩토링을 해봐도 괜찮을 것 같아요.

### 변수 및 함수 명명 규칙

#### Python

- 파일명: 소문자와 밑줄(\_)을 사용합니다.

  > - 예시: main.py, database_utils.py, test_app.py

- 변수명: 스네이크 케이스(snake_case)를 사용합니다.

  > - 예시: user_id, shopping_cart, load_profile

- 함수명: 스네이크 케이스(snake_case)를 사용합니다.
  > - 예시: calculate_price(), get_data(), render_view()

#### HTML/CSS

- 파일명:소문자와 하이픈(-)을 사용합니다.

  > - 예시: index.html, contact-form.html, style.css, main-layout.css

- 클래스명은 소문자와 하이픈(-)을 사용합니다.

  > - 예시: .btn-primary, .navigation-bar

- ID는 일반적으로 카멜 케이스(camelCase)를 사용합니다.

  > - 예: #mainContent

#### JavaScript

- 파일명: 소문자와 하이픈(-)을 사용합니다.

  > - 예시: app.js, my-script.js, form-validator.js

- 변수명: 카멜 케이스(camelCase)를 사용합니다.

  > - 예시: userName, shoppingCart, loadProfile

- 함수명: 카멜 케이스(camelCase)를 사용합니다. 동사로 시작하는 것이 일반적입니다.

  > - 예시: calculatePrice(), getData(), renderView()

### 주석 및 문서화

- 코드의 목적과 복잡한 로직은 주석을 통해 명확히 설명해야 합니다.
- 주석으로 설명이 어렵고, 전반적으로 설명이 필요하다면 `[본인의 이름.md]`에 설명을 작성해주세요.

## 5. 자주 발생하는 문제

- 배가 고파요. 😣
  > - 밥을 먹도록 합니다. 😯

## 6. 참고 자료

### 목소리 모델링의 기본 플로우

![Data flow](/description_images/data-flow.PNG)

### voice-changer를 docker로 설치하기

#### 1. wsl 설치

- wsl 설치하기

```bash
wsl --install
```

- ubuntu 설치/재시작

```bash
wsl --install -d ubuntu
```

- wsl 설치 확인

```bash
wsl --list
```

#### 2. docker desktop 설치/재시작 및 wsl와 통합하기 [[참고]](https://www.youtube.com/watch?v=POo_Cg0eFMU)

- docker desktop에서 설치하기

- 현재 사용자를 docker 그룹에 추가하기
  sudo usermod -aG docker $USER

- docker 설치 확인: docker 관련된 게 아래에 뜸

```bash
wsl --list
```

#### 3. git clone

- git 모듈 다운로드: Linux git으로 clone으로 해야 띄어쓰기 이슈 예방 가능. Windows의 git pull이랑 Linux의 git pull을 했을 때, 띄어쓰기 방식이 다름.

```bash
sudo apt-get install git
```

- git clone

```bash
git clone https://github.com/w-okada/voice-changer.git
```

- git clone 한 폴더 내부로 이동하기

```bash
cd [path]
```

#### 4. 프로그램 실행

- 도커를 사용해서 프로그램 실행하기: 저희 노트북에는 GPU가 없어요. 😢

```bash
USE_GPU=off bash start_docker.sh
```
