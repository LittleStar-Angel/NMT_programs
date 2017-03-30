# -*- coding: utf-8 -*-
from tasks.translate import Translator
task = {'action': 'translate', 'targetLang': u'zh', 'sourceLang': u'en', 'text': "鼎盛旅游服务有限公司".decode('utf8')}
print Translator('2006', 'zh', 'en').process_task(task)