개발 방법 전체 내용은 notion 페이지를 참조한다.
https://www.notion.so/aiteamkr/1-97af36d9ef9b4130978a985270deb9e7


##Usage
###0) mmdetection benchmark 설치: tools 밑에 mmdetection 이름으로 설치 권장 
###1) 이미지 폴더 준비 
   config/globalconfig.json에서 [NETWORK] - [TEST] - [BASE_DIR]에 video folder 정의
###2) model configuration 파일 및 checkpoint path 설정
   argparse의 argument 중 config, checkpoint의 경로를 원하는 네트워크 모델로 설정할 것
###3) python tools/demo.py
   실행시 결과 파일 val_results/json/내에 sequence 번호.json 파일로 결과 파일 생성됨
   
    
    
