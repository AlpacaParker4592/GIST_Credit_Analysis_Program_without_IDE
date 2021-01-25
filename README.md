# GIST Credit Analysis Program *beta*(without IDE)

GIST 학점 분석 프로그램을 이용해주셔서 감사합니다. 이 프로그램은 GIST대학 학부생을 대상으로 본인의 이수 학점, 평점, 졸업요건 확인을 위한 프로그램이며, Python을 설치하지 않으신 분들도 사용할 수 있는 버전의 프로그램입니다. 해당 프로그램의 소스코드 요구 시 하단의 메일로 연락 주시면 신분 확인 후 보내드리겠습니다.

![Installation_Process](https://user-images.githubusercontent.com/63055303/104684734-0137fc80-573d-11eb-9467-3e4653896b87.PNG)

## Execution Process
1. Code 버튼을 눌러 해당 폴더를 zip 파일로 내려받으십시오.
2. 압축을 풀고 Design File/GIST_Credit_Analysis_Program.exe를 실행하십시오.
3. 절차에 따라 실행하시면 귀하의 학점분석 그래프를 보실 수 있습니다.
   * 현재 제공 데이터: 현재 취득 학점 및 졸업 요건 달성 현황, 전체 및 전공 평균 평점, 달성/미달성한 졸업 요건, 분야별 부전공 달성 현황

![Result2](https://user-images.githubusercontent.com/63055303/103453828-4c0b4a80-4d21-11eb-832c-9f5a65797205.PNG)

## Precautions for Users

### 프로그램 이용 관련
* 현재 테스트가 충분히 이뤄지지 않아 버그가 있을 수 있습니다. 이 점 양해 부탁드리며 버그 발생 시 아래 이메일로 제보 주시면 감사하겠습니다.
* 해당 프로그램에서 나온 결과는 **귀하의 졸업을 보장하지 않습니다.** 어디까지나 참고용으로만 사용하시길 바랍니다.
* 해당 프로그램은 **14~20학번 학부생**만 사용 가능합니다. 현재 학사편람이 나오지 않은 관계로 21학번 학부생은 사용이 불가능합니다.
    * 현재 재학 중인 19~20학번 학부생만 실행 확인이 되었으며, 그 이외 학번 재학생, 휴학 중인 학부생은 확인되지 않았습니다.
* 이 프로그램은 귀하의 졸업 요건을 그래프로 나타내기 쉽도록 졸업 요건 일부를 통합했으며, 귀하께서 수강(이수)한 교과목을 전체적으로 출력하지 않습니다.
정확한 졸업 요건이나 지금까지 이수한 교과목 전체를 알고자 하는 경우에는 다음 프로그램 URL을 참고하시길 바랍니다.
    * https://colab.research.google.com/drive/1pRaZLyTsbN9RIpmoCs-645dxTWQDM_LQ?usp=sharing&fbclid=IwAR0yx6ptBulpYTaRz9zea9JW7H617tWE518gcrUqDlzWDYFdH73gwfopQ-A
    * https://github.com/wannagraduation/graduation_requirement
* 해당 프로그램을 처음 실행 시 **Windows의 PC 보호** 창이 뜰 수 있습니다(Windows 운영 체제만 해당).
"추가 정보"를 눌러 나온 "실행" 버튼을 클릭해야 프로그램이 진행됩니다.
    * 그러나 만일 위 프로그램을 신뢰하지 않는 경우 해당 프로그램을 실행하지 마십시오.
* 해당 프로그램은 ZEUS에 로그인하기 위한 목적으로 귀하의 **ID와 비밀번호**가 사용됩니다.
해당 ID와 비밀번호는 프로그램이 실행되는 동안 암호화 과정을 거쳐 edited/info 폴더에 personalinfo.xlsx 파일로 저장됩니다(프로그램 종료 시 해당 파일은 자동 삭제됩니다.).
    * 귀하의 정보가 웹상으로 업로드되지 않지만, 마찬가지로 위 프로그램을 신뢰하지 않는 경우 해당 프로그램을 실행하지 마십시오.
* 현재 해당 프로그램은 Windows에서만 작동 확인이 되었으며, 이외 운영체제(iOS, Linux 등)에서는 확인되지 않았습니다.


### 수강 과목 관련
* 교양 과목 분류(HUS, PPE, GSC)의 경우 **각 연도별** 학사편람을 참고하여 제작하였습니다.
이때 연도에 따라 과목 분류가 달라지는 경우가 발견됐습니다(ex. 강대국의 흥망: 2018년에 GSC에서 HUS로 변경). 이에 대해서는 다음과 같습니다.
  > 분류가 잘못된 과목이 있을 수 있습니다. 예를 들어 'GS2601: 동아시아의 전통과 현대' 과목의 경우 2016 학사편람 기준으로는 GSC로 분류, 2017 - 2020 학사편람 기준으로는 HUS로 분류됩니다...(후략)
  > * (2020.07.10) 학사지원팀에 이에 대해 문의해본 결과 그러한 과목 모두에 **일률적으로 적용되는 규칙은 없다**는 말씀을 전달받았습니다(각각 해당 수업을 수강한 년도의 학사편람을 따를수도 있으며 분류 중 한 가지를 자유롭게 선택할 수도 있는 등)...(후략)
  > 
  > \- 위의 [Google Colab 졸업요건 분석 프로그램](https://colab.research.google.com/drive/1pRaZLyTsbN9RIpmoCs-645dxTWQDM_LQ?usp=sharing&fbclid=IwAR0yx6ptBulpYTaRz9zea9JW7H617tWE518gcrUqDlzWDYFdH73gwfopQ-A) 설명에서 일부 인용
    * 해당 프로그램은 교양 과목을 수강한 년도를 반영하여 교양 과목을 분류하는 방법을 사용했습니다.
        * ex. "강대국의 흥망" 과목을 2017년 이전에 수강하면 GSC, 2018년 이후에 수강하면 HUS로 반영
* 계절학기 과목의 성적은 직전 학기의 성적에 반영되도록 처리했습니다(여름학기: 봄학기, 겨울학기: 가을학기).
* AP 과목의 성적은 1학년 1학기의 성적에 반영되도록 처리했습니다. 해당 과목은 모두 S 처리되므로 평점(GPA)에 반영되지 않습니다.
* 현재 일부 교과목(주로 부전공으로 인정되는 교과목)에 대해 코드쉐어를 반영하고 있습니다.
현재 이 프로그램에서 코드쉐어를 반영하는 조건은 다음과 같습니다(2021.01.17 기준).
빠진 부분은 추후 업데이트에서 추가하겠습니다.
    * 전공 교과목: 각 (부)전공 교과목 코드에 대해 대부분 반영됨.
    * 부전공 교과목: GSxxxx 및 각 (부)전공 교과목 코드에 대해 대부분 반영됨.
    * 교양 과목: GSxxxx 코드만 인정(현재 각 부전공 교과목 코드는 인정하지 않음. 추후 업데이트 예정).
        * ex1-1. 교양 과목인 "현대 예술의 이해" 과목을 GS로 이수 시
            * 교양 학점(GS만 인정): +3
            * 문화기술 부전공 학점(GS, CT 모두 인정): +3
        * ex1-2. 같은 과목을 CT로 이수 시
            * 교양 학점: **+0**
            * 문화기술 부전공 학점: +3
        * ex2-1. 전컴 선택 과목인 "컴퓨터 그래픽스" 과목을 EC로 이수 시
            * 전컴 (부)전공 학점(EC, CT 모두 인정): +3
            * 문화기술 부전공 학점(CT, EC 모두 인정): +3
        * ex2-2. 전컴 선택 과목인 "컴퓨터 그래픽스" 과목을 CT로 이수 시
            * 전컴 (부)전공 학점: +3
            * 문화기술 부전공 학점: +3
* 실행 중 오류가 발생하거나 나온 결과가 실제 반영되는 학점과 다른 사항을 발견할 시 lhh-znso4 (at) gm.gist.ac.kr로 연락 바랍니다.

## Update Status
* 교양 과목 DB 제공 범위: 2014 ~ 2020년

## Release Notes
### 0.2.1 버전(2021.01.17)
* 일부 코드쉐어 인정 교과목 추가

#### Future Works
* 복수전공 달성 현황 관련 데이터 제공
* 버그 수정
    * 재수강 목적으로 현재 수강한 과목과 성적표에 나와 있는 과목(C+~D0) 학점이 합쳐져 나오는 버그
    * 프로그램 실행 경로명(계정명 포함)에 유니코드(한글 등) 있을 시 결과창이 나오지 않는 버그(QtWebProcess 문제로 추정)
        * 프로그램 용량 증가(대략 200->450MB) 문제 때문에 고민 중
        * 현재 버전은 Plotly 자체 기능으로 상단 그림처럼 html이 자동으로 열리게끔 하여 임시적으로 해결
    
![Result](https://user-images.githubusercontent.com/63055303/105740697-c889f580-5f7c-11eb-9ac4-ee25693388aa.PNG)

### 0.2.0 버전(2021.01.14)
* 부전공(7개 주전공 관련 및 이외 분야) 달성 현황 데이터 제공 기능 추가
* 교양 과목 업데이트 기능 구현(HUS, PPE 적용 포함, Update Status 참고)
* AP과정 이수 과목 및 계절학기 이수 과목 인식 정상화

### 0.1.0 버전(2021.01.01)
* 초기 개발 완료
