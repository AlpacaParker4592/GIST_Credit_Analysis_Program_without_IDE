# GIST Credit Analysis Program *beta*(without IDE)

GIST 학점 분석 프로그램을 이용해주셔서 감사드립니다. 이 프로그램은 GIST대학 학부생을 대상으로 본인의 이수 학점, 평점, 졸업요건 확인을 위한 프로그램이며, Python IDE를 설치하지 않으신 분들도 사용할 수 있는 버전의 프로그램입니다.

![Installation_Process](https://user-images.githubusercontent.com/63055303/103422053-dc8f4100-4be2-11eb-939e-417eee11afae.PNG)

## Execution Process
1. Code 버튼을 눌러 해당 폴더를 zip 파일로 내려받으십시오.
2. 압축을 풀고 Design File/GIST_Credit_Analysis_Program.exe를 실행하십시오.
3. 절차에 따라 실행하시면 귀하의 학점분석 그래프를 보실 수 있습니다.
   * 현재 제공 사항: 현재 취득 학점 및 졸업 요건 달성 현황, 전체 및 전공 평균 평점, 달성/미달성한 졸업 요건

![Result2](https://user-images.githubusercontent.com/63055303/103453828-4c0b4a80-4d21-11eb-832c-9f5a65797205.PNG)

## Precautions for Users
* 해당 프로그램은 **14~20학번 학부생**만 사용 가능합니다. 타대학 출신 대학원생은 사용이 불가능합니다.
    * 현재 재학 중인 19~20학번 학부생만 실행 확인이 되었으며, 그 이외 학번 재학생, 휴학 중, 졸업 이후의 학부생(대학원생 포함)은 확인되지 않았습니다.
* 현재 해당 프로그램은 Windows에서만 작동 확인이 되었으며, 이외 운영체제(iOS, Linux 등)에서는 확인되지 않았습니다.
* Step 2 진행 시 처음 진행하실 때 Python 실행과 관련하여 네트워크 관련 창이 뜰 것입니다. 이때 허용 버튼을 눌러야 프로그램이 원활히 진행됩니다.
* 해당 프로그램은 ZEUS에 로그인하기 위한 목적으로 귀하의 ID와 비밀번호가 사용됩니다.
해당 ID와 비밀번호는 프로그램이 실행되는 동안 암호화(AES) 과정을 거쳐 edited/info 폴더에 personalinfo.xlsx 파일로 저장됩니다(프로그램 종료 시 해당 파일은 자동 삭제됩니다.).
    * 귀하의 정보가 웹상으로 업로드되지 않지만, 만일 위 프로그램을 신뢰하지 않는 경우 해당 프로그램을 실행하지 마십시오.
* 교양 과목 분류(HUS, PPE, GSC)의 경우 **각 년도별** 학사편람을 참고하여 제작하였습니다.
이때 년도에 따라 과목 분류가 달라지는 경우가 발견되었으므로(ex. 강대국의 흥망: 2018년에 GSC에서 HUS로 변경), 정확한 교양 과목 분류는 담당 부서에 연락하시길 바랍니다.
    * 해당 프로그램은 교양 과목을 수강한 년도를 반영하여 교양 과목을 분류하는 방법을 사용했습니다.
        * ex. "강대국의 흥망" 과목을 2017년 이전에 수강하면 GSC, 2018년 이후에 수강하면 HUS로 반영
* 계절학기 과목의 성적은 직전 학기의 성적에 귀속됩니다(여름학기: 봄학기, 겨울학기: 가을학기).
* 15학번 학부생의 경우 HUS, PPE 과목 수강 의무 여부를 알 수 없어 임시로 그 요소를 제외한 채 분석하도록 했습니다(14학번 이전은 HUS, PPE 과목 수강 의무 없음).
* 실행 중 오류가 발생하거나 나온 결과가 실제 반영되는 학점과 다른 사항을 발견할 시 lhh-znso4@gm.gist.ac.kr로 연락 바랍니다.

## Update Status
* 전체 DB: 2020.08.27 업데이트(사용자 개인 업데이트 가능)
* 교양 과목 DB: 2020년도 업데이트

## Release Notes
### 0.1.0 버전(2021.01.01)
초기 개발 완료
#### Future Works
* 부전공/복수전공 달성 현황 관련 데이터 제공
* 버그 수정(현재 재수강 목적으로 수강한 과목과 성적표에 나와 있는 과목(C+~D+) 학점이 합쳐져 나오는 버그)
