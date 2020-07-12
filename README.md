# Installation
```
ruby -v
# ruby 2.4.10p364 (2020-03-31 revision 67879) [x64-mingw32]
bundle install
ruby alggago.rb
```

# Adjustment for Python ai

`ai_black.rb`에서 positions 을 `temp.json` 파일로 작성하고 `py_ai_sample.py`를 실행, `py_ai_sample.py`에서는 저장된 json 파일을 읽어 `print` 함수로 ruby 프로세스에 돌려주는 방식으로 작성되었음. `py_ai_sample.py`의 알고리즘은 원래 ruby로 작성되어 있던 것과 같음

# 기타
- 윈도우에서 정상 실행 가능
- 한글 폰트 깨짐 문제 있음(R: 새로 시작하기, P: 턴 넘기기, N: 다음 턴 연산하기)
