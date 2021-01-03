import os
import sys
import csv
import datetime
from redminelib import Redmine

#定義
SERVER_URL = 'http://sv3003'
API_KEY = '279948022c547ea29b7a613589d062f7637ea2e9'
OUT_FILE = 'redmine.csv'

#関数定義(チケット一覧取得)
def get_ticket():
    redmine = Redmine(SERVER_URL, key=API_KEY)
    issues = redmine.issue.all(sort='category:desc')
    #issues = redmine.issue.filter(assigned_to_id='!me')
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open(datetime.date.today().strftime('%Y-%m-%d') + '_' + OUT_FILE, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['プロジェクト名', 'チケット名','チケットID','日付','時間(0は処理しない)','コメント','活動(数字のみ残す)'])
        for issue in issues:
            writer.writerow([issue.project.name,issue.subject,issue.id,datetime.date.today().strftime('%Y/%m/%d'),0,'','11:調査/9:開発/10:運用/12:その他'])

#関数定義(稼働時間セット)
def set_ticket_time(file_path):
    if(os.path.exists(file_path)):
        with open(file_path,'r') as f:
            reader = csv.reader(f)
            line = [row for row in reader]
            redmine = Redmine(SERVER_URL, key=API_KEY)
            for i in range(len(line)):
                if i > 0:
                    if int(line[i][4]) > 0:
                        if line[i][6].isdecimal() == True:
                            time_entry = redmine.time_entry.new()
                            time_entry.issue_id = line[i][2]
                            tdatetime = datetime.datetime.strptime(line[i][3], '%Y/%m/%d')
                            time_entry.spent_on = datetime.date(tdatetime.year, tdatetime.month, tdatetime.day)
                            time_entry.hours = line[i][4]
                            if len(line[i][5]) > 0:
                                time_entry.comments = line[i][5]
                            time_entry.activity_id = line[i][6]
                            time_entry.save()
        
        print('完了')


#メイン処理(引数あり→チケット取得：引数なし→時間セット)
if len(sys.argv) >= 2:
    set_ticket_time(sys.argv[1])
else:
    get_ticket()

