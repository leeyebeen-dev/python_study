
참고 사이트 : https://nbviewer.org/github/SDRLurker/deep-learning/blob/master/1%EC%9E%A5.ipynb 

# 헬로 파이썬

## 1. 파이썬이란?

간단하고 배우기 쉬운 프로그래밍 언어. 오픈소스
영어와 유사한 문법. 불편한 컴파일 과정 없음

* 데이터 과학 분야 : 수치 계산과 통계 처리를 다루는 라이브러리. Numpy, SciPy
* 딥러닝 프레임워크 API : TensorFlow, Caffe, Chainer, Theano

## 2. 파이썬 설치하기

* 자주 사용할 외부 라이브러리 : Numpy, matplotlib

    * Numpy : 수치 계산용 라이브러리
    * matplotlib : 그래프를 그려주는 라이브러리

* 아나콘다 배포판

## 3. 파이썬 인터프리터

* 파이썬 버전 확인 : `python --version`

* 산술 연산
* 자료형
* 변수
* 리스트
* 딕셔너리
* bool
* if문
* for문
* 함수

## 4. 파이썬 스크립트 파일

파이썬 프로그램을 파일로 저장. 그 파일을 함께 실행하는 방법이 있음

* 파일로 저장하기

```shell
$ cd 디렉터리 경로
$ python test.py
```

* 클래스

개발자가 직접 클래스를 정의하면 독자적인 자료형을 만들 수 있음
클래스만의 전용 함수와 속성을 정의

```python
class 클래스이름:
    def __init__(self, 인수, ...): # 생성자
        ...
    def 메서드이름1(self, 인수, ...): # 메서드 1
        ...
    def 메서드이름2(self, 인수, ...): # 메서드 2
        ...
```

--> _init_ : 생성자 클래스를 초기화하는 방법을 정의. 인스턴스가 만들어질 때 한 번만 불림.
--> self : 자신을 나타냄. 파이썬에서는 메서드의 첫 번째 인수로 self를 명시적으로 사용함.

## 5. Numpy

numpy.array : 배열 클래스. 딥러닝 구현 시 배열, 행렬 계산에 많이 사용.

`import numpy as np`

## 6. matplotlib

그래프를 그리기 위한 라이브러리. 그래프 그리기와 데이터 시각화를 쉽게
