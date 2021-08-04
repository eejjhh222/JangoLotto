<h1>로또번호 분석기</h1>
<ul>
    <li>로또번호 크롤링</li>
    <li>로또번호 DB CRU</li>
    <li>로또번호 list</li>
    <li>Pandas 데이터분석</li>
</ul>



<h1>python 자주 쓰는 명령어</h1>>
<h5>package 관련 명령어</h5>
<ul>
    <li>pip freeze > requirements.txt</li>
    <li>pip install -r requirements.txt</li>
    <li>pip install --upgrade pip</li>
</ul>
<h5>django 관련 명령어</h5>
<ul>
    <li>python manage.py {cmd} : 기본 명령어 형태</li>
    <li>runserver 8000 : 가상서버 실행</li>
    <li>startapp : app 생성</li>
    <li>createsuperuser : 관리자 생성</li>
    <li>makemigrations {app} -app : app의 모델 변경사항 체크</li>
    <li>migrate : 변경 사항을 DB에 반영</li>
    <li>collectstatic : static파일을 한 곳에 모음</li>
    <li>shell : 쉘을 통해 데이터를 확인</li>
</ul>

<h1>Templates 경로</h1>
<p>공통 html파일 경로 /templates</p>
<p>App별 html파일 경로 {App}/templates</p>
<p>기본적으로는 setting.py에 TEMPLATES 에서 설정한 최상위 templates경로를 지정하지만,</p>
<p>최상위의 templates폴더에 파일이 없으면 해당앱의 templates폴더를 조회한다.</p>


<h1>버전업에따른 추가명령어</h1>
<p>pip install djangorestframework</p>
<p>pip install django</p>