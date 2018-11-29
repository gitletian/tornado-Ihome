# coding=utf-8

from .CCPRestSDK import REST

import configparser
import logging

#���ʺ�
accountSid= '8aaf0708568d4143015697b0f4960888';

#���ʺ�Token
accountToken= '42d3191f0e6745d6a9ddc6c795da0bed';

#Ӧ��Id
appId='8aaf0708568d4143015697b0f56e088f';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort='8883';

#REST�汾��
softVersion='2013-12-26';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id

# def sendTemplateSMS(to,datas,tempId):
#
#
#     #��ʼ��REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)


class CCP(object):

    def __init__(self):
        self.rest = REST(serverIP, serverPort, softVersion)
        self.rest.setAccount(accountSid, accountToken)
        self.rest.setAppId(appId)

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def sendTemplateSMS(self, to, datas, tempId):
        return self.rest.sendTemplateSMS(to, datas, tempId)
        # try:
        #     result = self.rest.sendTemplateSMS(to, datas, tempId)
        # except Exception as e:
        #     logging.error(e)
        #     raise e

        # # print result
        # # for k, v in result.iteritems():
        # #     if k == 'templateSMS':
        # #         for k, s in v.iteritems():
        # #             print '%s:%s' % (k, s)
        # #     else:
        # #         print '%s:%s' % (k, v)
        # if result.get("statusCode") == "000000":
        #     return True
        # else:
        #     return False

ccp = CCP.instance()

if __name__ == "__main__":
    ccp.sendTemplateSMS("18516952650", ["1234", 5], 1)



   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)