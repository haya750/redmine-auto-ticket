import sys
from redminelib import Redmine

#定義
SERVER_URL = 'http://sv3003'
API_KEY = '279948022c547ea29b7a613589d062f7637ea2e9'

redmine = Redmine(SERVER_URL, key=API_KEY)
#チケットIDで検索
time_entries = redmine.time_entry.filter(issue_id = sys.argv[1])
for t in time_entries:
    print('  ID:%d' % t.id)
    print('  活動:%s' % t.activity)
    print('  コメント:%s' % str(t.comments))
    print('  作成日:%s' % t.created_on)
    print('  時間:%s' %t.hours)
    print('  チケットID:%s' % t.issue)
    print('  プロジェクトID:%s' % t.project)
    print('  日付:%s' % t.spent_on)
    print('  更新日:%s' % t.updated_on)
    print('  user:%d %s' % (t.user.id,t.user.name))
    print('  作業分類 %d %s' % (t.activity.id, t.activity.name))
