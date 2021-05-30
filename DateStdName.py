# -*- coding: utf-8 -*-
"""
Created on Fri May 28 23:33:05 2021

@author: HY Park
module name : DB에 날짜, 학생이름, 교재정보 저장
DateStdName class 정의

"""

import datetime

class DateStdName:
    def __init__(self, DateStr, StdName, BookInfo):
        self.DateStr = DateStr
        self.StdName = StdName
        self.BookInfo = BookList_sel() # 교재 선택 module로부터 정보 받아옴
        
    def getDate(whattime):
        # 날짜 정보 받아오는 함수
        if (whattime=="now") :
            DateStr = datetime.datetime.now()
        else :
            DateStr = input("날짜 입력(ex: 210101) : " )
            # input 웹의 날짜 select 창으로 바꾸기
        return DateStr
        
    def getStdName():
        #학생 이름 입력받기
        StdName = input("학생 이름 입력 : " )
        # input 웹 상의 Charfield로 바꾸기
        return StdName

"""
 < test code >
name=DateStdName.getStdName()
print(name)
date=DateStdName.getDate("select")
print(date)
"""