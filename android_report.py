# _*_ coding:utf-8 _*_

from pyquery import PyQuery as pq
import sys,os

file_path =  sys.argv[1]
class ParseReport():
    
    succeed = 0
    failed = 0    
    s_suit = {}
    f_suit = {}
    
    def goParse(self):
        if not os.path.exists(file_path):
            return
        with open(file_path,'r+') as f:
            result = f.read()
        doc = pq(result)
        d_testsuite = doc('testsuite')
        for suite in d_testsuite:
            flag = True
            suit_name = pq(suite).attr('name')
            d_case = pq(suite)('testcase')  
            list_case = []
            list_case_f = []
            for case in d_case:
                if str(pq(case).find('failure'))!='':
                    flag = False
                dict_case = None
                dict_case_f = None
                if(flag == False):
                    dict_case_f = {pq(case).attr('name'):pq(pq(case).find('failure')).text()}
                    self.failed += 1
                    flag= True
                else:
                    dict_case = {pq(case).attr('name'):pq(case).attr('time')}
                    self.succeed += 1
                if dict_case!=None:
                    list_case.append(dict_case)
                if dict_case_f!=None:
                    list_case_f.append(dict_case_f)
            if list_case!=[]:
                self.s_suit[suit_name]=list_case
            if list_case_f!=[]:
                self.f_suit[suit_name]=list_case_f   
        print '------------------------------------'
        print '-->结果<--','\n',self.succeed,'条通过','\n',self.failed,'条失败\n','成功率:',str((float(self.succeed)/(self.succeed+self.failed))*100)[0:5],'%','\n'
        print '------------------------------------'
        print '失败用例:'
        for k,v in self.f_suit.items():
            print '用例名:',k
            for _case in v:
                for kk,vv in _case.items():
                    print '方法名:',kk,'\n日志:\n',vv
            print '--'
        print '------------------------------------'
        print '成功用例:'
        for k,v in self.s_suit.items():
            print '用例名:',k
            for _case in v:
                for kk,vv in _case.items():
                    print '方法名:',kk,'  执行时间:',vv 
            print '--'
        
ParseReport().goParse()


