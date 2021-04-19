<h1 align="center"> Web Scrapper with Python</h1>
<p align="center">
  <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=HTML5&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=CSS3&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Python3-3766AB?style=flat-square&logo=Python&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=Flask&logoColor=white"/></a>
  <img src="https://img.shields.io/badge/repl.it-667881?style=flat-square&logo=repl.it&logoColor=white"/></a>
</p>
<br/>
<p align="center">Python으로 웹 스크래퍼 만들기 강의를 수강하며 실습한 코드입니다</p>
<p align="center">2021-03-21 ~ 2021-04-04 강의 수강<br/>2021-03-29 ~ 2021-04-12 챌린지</p> 
<p align="center">
<img width="400" alt="스크린샷 2021-04-12 오후 6 42 02" src="https://user-images.githubusercontent.com/80886445/114555486-b594e080-9ca2-11eb-91da-8619cb90bcdd.png">
</p>

## 🗂 폴더 구조
* Indeed와 Stackoverflow 사이트에서 채용 공고를 스크래핑하고 .csv 파일로 다운로드하는 코드입니다.
* scrapper_with_Flask : 기존 코드에 Flask를 연동하여 스크래핑한 데이터를 웹 페이지에 표시하는 웹 스크래퍼 코드입니다.
* Code_Challenge : python 2주 챌린지를 진행하며 수행했던 과제 폴더입니다.


## 📦 패키지
* requests version 2.25.1 (Python HTTP for Humans.)
* BeautifulSoup version 4.9.3 (Screen-scraping library)
* Flask version 1.1.2 (A simple framework for building complex web applications.)


## ➰ Code Challenge 졸업 과제 
- Find Remote Jobs 메인 페이지
<img width="500" alt="스크린샷 2021-04-13 오후 10 22 18" src="https://user-images.githubusercontent.com/80886445/114562797-cb59d400-9ca9-11eb-9ecd-08aef77486a7.png">

- 검색창에 키워드 입력 시, Stackoverflow.com, weworkremotely.com, remoteok.io 사이트에서 해당 키워드의 채용 공고를 스크래핑 합니다. 
- 스크래핑이 완료되면 Scroll Down. Please 문구가 제공되며, 하단에 채용 공고 목록이 조회됩니다.
- 한 번 스크래핑을 수행하면 해당 목록이 리스트에 저장되어 같은 키워드로 조회 시 스크래핑을 수행하지 않고 리스트에 저장된 목록을 불러와 조회하는 데 걸리는 시간이 단축됩니다.
<div>
<img width="500" alt="스크린샷 2021-04-13 오후 10 23 58" src="https://user-images.githubusercontent.com/80886445/114563503-6b176200-9caa-11eb-85d7-ff2efa788879.png">
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 05" src="https://user-images.githubusercontent.com/80886445/114563743-a6b22c00-9caa-11eb-95ae-03f1382e2331.png">
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 15" src="https://user-images.githubusercontent.com/80886445/114563807-b5004800-9caa-11eb-8e0b-e4f8c9061d5a.png">
</div>

- 각 채용 공고 Apply Link의 url을 클릭하면 해당 채용 공고 페이지가 제공됩니다.
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 28" src="https://user-images.githubusercontent.com/80886445/114563997-e1b45f80-9caa-11eb-8589-3bf9324a3c2a.png">

- 상단의 export 버튼을 누르면 채용 공고 목록이 .csv 파일로 다운로드 됩니다. 
<div>
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 05" src="https://user-images.githubusercontent.com/80886445/114564733-90f13680-9cab-11eb-83ea-a0cba8af7cf9.png">
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 36" src="https://user-images.githubusercontent.com/80886445/114564070-f264d580-9caa-11eb-89d6-0882c52e97cd.png">
</div>

- 상단의 clear 버튼을 누르면 Find Remote Jobs 메인 페이지로 이동합니다
<div>
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 05" src="https://user-images.githubusercontent.com/80886445/114564767-98b0db00-9cab-11eb-8fb8-3c44be18f4b5.png">
<img width="500" alt="스크린샷 2021-04-13 오후 10 24 44" src="https://user-images.githubusercontent.com/80886445/114564200-12949480-9cab-11eb-95a0-6b89b7320c17.png">
</div>

## 🎓 졸업
<img width="400" alt="스크린샷 2021-04-20 오전 2 40 53" src="https://user-images.githubusercontent.com/80886445/115279601-e5038b80-a181-11eb-852a-d9b20c20fde2.png">


