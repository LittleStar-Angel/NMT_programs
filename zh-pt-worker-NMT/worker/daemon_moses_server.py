# -*- coding: utf-8 -*-
'''
Created on Feb 10, 2015

@author: peter
'''
import os
import subprocess
from tasks.translate import Translator
import logging
import time
class daemon_moses_server():
    def __init__(self,src_sentence,tgt_sentence,logger):
        self.test_sentence = src_sentence
        self.result_sentence = tgt_sentence
        self.logger = logger
    def check_moses_server(self,test_sentence,result_sentence):
        data = test_sentence
        task = {'action': 'translate', 'targetLang': u'zh', 'sourceLang': u'en', 'text': test_sentence}
        try:
            translator = Translator('2006', 'zh', 'en')
            result = translator.process_task(task)
            translation_result = result['translation'][0]['translated'][0]['text']
            if translation_result == result_sentence:
                return True
        except:
            return False
    def kill_moses_server(self):
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        passwd = 'gtct0730'
        for line in out.splitlines():
            if 'mosesserver' in line:
                pid = int(line.split(None, 1)[0])
                cmd = 'echo %s|sudo -S kill %d' %  (passwd,pid)
                p = subprocess.call(cmd, shell=True)
                self.logger.info('killed corrupt process pid = %d' %pid)
    def start_moses_server(self):
        passwd = 'gtct0730'
        os.chdir(os.getcwd())
        cmd = 'echo %s|sudo -S -u root ../scripts/run_moses' %passwd
        starttime = time.time()
        p = subprocess.call(cmd, shell=True)
        costime = time.time() - starttime
        self.logger.info('start moses server succeed, cost time %s' %costime)
    def loop(self,timestep):
        import time
        iter = 0
        while True:
            current_state = self.check_moses_server(self.test_sentence, self.result_sentence)
            # print iter
            if current_state == False:
                self.logger.info('error has been detected in moses server, now restart it')
                self.kill_moses_server()
                self.start_moses_server()
            iter += 1
            time.sleep(timestep)
    def __main__(self):
        # self.kill_moses_server()
#         self.start_moses_server()
        self.loop(600)
if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(name)s %(message)s'
    logging.basicConfig(filename = os.path.join(os.getcwd(), 'daemon_moses_server.log'), level = logging.DEBUG,format=FORMAT)
    logger = logging.getLogger('daemon_moses_server')
    my_daemon = daemon_moses_server(u'我是中国人','i am a chinese',logger)
    my_daemon.__main__()