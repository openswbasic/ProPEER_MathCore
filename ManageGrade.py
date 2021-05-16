"""

team: ProPEER
project: MathCore
writer: Chaerin Jung

Grade Management Module

"""

import pandas as pd


def StdInfo():
    
    stdinfo = pd.read_excel('여기에 저장된 엑셀파일 경로를 입력')
    stdinfo
    
def StdSort():
    
    stdinfo = pd.read_excel('여기에 저장된 엑셀파일 경로를 입력')
    
    select = input('정렬방법을 선택하세요: ')
    
    if select == '날짜순':
        stdinfo.sort_values(by='날짜')
    
    else:
        stdinfo.sort_values(by='이름')
    