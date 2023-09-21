# RansomwareDetectAI
이 모델은 엄청납니다!  XGBoost를 활용한 랜섬웨어를 탐지하는 모델!
<br>
<br>

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

# 사용법
python &nbsp; this_file_is.py &nbsp; {directory_path} <br>
<br>
검증하고 싶은 랜섬웨어의 디렉토리 경로를 넣어줍니다.

