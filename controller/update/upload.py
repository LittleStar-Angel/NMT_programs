from flask import Flask, request, render_template,redirect, url_for,flash, abort, Response, jsonify
import logging;
import os;

app = Flask(__name__, static_url_path='')

#


@app.route('/regmodel', methods=['POST'])
def updatere():
    messg = None
    if request.method == 'POST':

        file = request.files['file']

    print('Start to update the ReModel dict')
    UPLOAD_FOLDER='/home/luyi/controller/appserver'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if file:
        filename = file.filename
        print(filename)
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save( UPLOAD_FOLDER+'/'+filename)
        messg = '<p style="text-align:center">Updated' + filename + '</p>'

        return messg
    else:
        messg = '<p style="text-align:center">Faild to Updata</p>'

        return messg

@app.route('/upptdict', methods=['POST'])
def updatept():
    if request.method == 'POST':
        file = request.files['file']

    print('Start to update the pt2zh dict')
    UPLOAD_FOLDER='/home/luyi/pt-zh-worker-v1/worker/generalization'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if file:
        filename = file.filename
        print(filename)
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save( UPLOAD_FOLDER+'/'+filename)
        messg = '<p style="text-align:center">Updated' + filename + '</p>'

        return messg
    else:
        messg = '<p style="text-align:center">Faild to Updata</p>'
        flash(messg)
        return messg

@app.route('/upzhdict', methods=['POST'])
def updatezh():
    if request.method == 'POST':
        file = request.files['file']

    print('Start to update the zh2pt dict')
    UPLOAD_FOLDER='/home/luyi/zh-pt-worker-v1/worker/generalization'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if file:
        filename = file.filename
        print(filename)
        print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save( UPLOAD_FOLDER+'/'+filename)
        messg = '<p style="text-align:center">Updated'+filename+'</p>'

        return messg
    else:
        messg = '<p style="text-align:center">Faild to Updata</p>'

        return messg

@app.route('/restart', methods=['POST'])
def restart():
    if request.method == 'POST':
        tt=request.form['Restart']

    if tt!='':
        print('Start to Restart the sever')

        PID_ptzh = open("/home/luyi/pt-zh-worker-v1/PID").readline().rstrip();
        PID_zhpt = open("/home/luyi/zh-pt-worker-v1/PID").readline().rstrip();
        PID_re = open("/home/luyi/controller/appserver/PID").readline().rstrip();
        os.system('kill ' + PID_ptzh);
        print('kill pt-zh:' + PID_ptzh);
        os.system('bash /home/luyi/pt-zh-worker-v1/scripts/run_worker');
        print('Restart pt-zh');
        os.system('kill ' + PID_zhpt)
        print('kill zh-pt:' + PID_zhpt);
        os.system('bash /home/luyi/zh-pt-worker-v1/scripts/run_worker');
        os.system('kill ' + PID_re);
        print('kill remodel:' + PID_re);
        os.system('bash /home/luyi/controller/scripts/run_ruletranslate');
        print('Restart remodel');


        messg = '<p style="text-align:center">Restarted</p>'

        return messg
    else:
        messg = '<p style="text-align:center">Faild</p>'

        return messg


@app.route('/')
def index():
    return render_template('index.html')


#
if __name__ == '__main__':
    app.secret_key = 'super secret key'

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(message)s")
    logger = logging.getLogger('updataserver')
    app.run(host="", port=32100);
