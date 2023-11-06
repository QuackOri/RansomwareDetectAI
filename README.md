# AI보안 기술개발 인력양성 : 악성코드 과정
* **해당 프로젝트는 KISIA 악성코드 탐지 AI모델 개발 교육과정에서 진행된 프로젝트입니다.**
* **팀원 : [QuackOri](https://github.com/QuackOri), [P4P3R-HAK](https://github.com/P4P3R-HAK), [tkdals69](https://github.com/tkdals69)**

# RansomwareDetectAI
**XGBoost를 사용하여 ransomware를 탐지하는 모델입니다.<br>
(PE파일 지원)**

# 구조
![image](https://github.com/QuackOri/RansomwareDetectAI/assets/103168837/dbcd7058-0edc-4317-904f-984bda2743b1)
<br>
<br>
RDS: Ransomware Defender System, Ransomware인지 아닌지 판단합니다. <br>
BDS: Binary Detect System, Malware인지 아닌지 판단합니다. <br>
<br>

Ransomware의 False Negative의 피해는 막중합니다.<br>
그래서 RDS의 FN의 피해가 최소화될 수 있도록 BDS가 보조합니다.<br>
만일 RDS에서 0이 나오더라도, BDS에서 1로 나온 파일은 주의해야 할 파일입니다.
<br><br>

# 필요 lib
    numpy
    pandas
    xgboost
    sklearn 1.2.2 (colab과 동일 버전)

# 사용법
> python &nbsp; this_file_is.py &nbsp; {directory_path} <br>
<br>
검증하고 싶은 랜섬웨어의 디렉토리 경로를 넣어줍니다.

# 결과화면
**정상파일**<br>
![image](https://github.com/QuackOri/RansomwareDetectAI/assets/52825485/deab4c61-41dd-4ece-bee3-796be01ed105)
<br><br>
**악성파일**<br>
![image](https://github.com/QuackOri/RansomwareDetectAI/assets/52825485/c0286644-56e1-43f7-8a29-361435d9d51c)
<br><br>
**랜섬웨어**<br>
![image](https://github.com/QuackOri/RansomwareDetectAI/assets/52825485/ed88ffeb-5444-49f2-98c2-e9506d286488)

# 탐지 기준
**정상파일 : It's Okay.. maybe**<br>
**의심되는 파일 : Warning!Warning!!Warning!!!** <br>
**랜섬웨어 : Stop! It's Dangerous**<br>
