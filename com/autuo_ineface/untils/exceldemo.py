#Excel表格操作


import xlrd
from xlutils.copy import copy

def readXLS():
#打开工作簿
  workbook=xlrd.open_workbook("../dataconfig/mtset.xlsx")

#获得一张表
  table=workbook.sheets()[0]

#打印表多少行
  print("一共%d行"%table.nrows)

#获取到某行某列
  content=table.cell_value(47,1)
  print(content)


def writeXLS():
#打开工作薄
   worke=xlrd.open_workbook("../dataconfig/mtset.xlsx")
#先把原数据复制过来
   write_worke=copy(worke)
#打开第一张表
   table=write_worke.get_sheet(0)
#往工作簿中写入内容
   table.write(47,1,"内容")
#保存数据
   write_worke.save("../dataconfig/mtset.xlsx")

#writeXLS()
readXLS()

class Test:
    def test(self):
       count=4
       count1=8
       print("通过个数%d,通过率%s%%"%(count,(count/count1)*100))

if __name__=='__main__':
    tes=Test()
    tes.test()
