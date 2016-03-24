# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import SelectMultipleField, SubmitField, validators, ValidationError, BooleanField, TextField, TextAreaField, RadioField
# basic flask modules
from flask import render_template, request, flash, session

from app import app
app.secret_key = 'dummy_key' # dont use this online!!!

import datetime

##############################################################################################


questionList = [u"1. Traten Sie aus Frust einen Gegenstand oder warfen ihn umher?",
                u"2. Fanden Sie Sportarten aufregender, in denen Blut floss?",
                u"3. Waren Sie so gereizt, dass Sie sich an anderen Menschen abreagierten?",
                u"4. Wollten Sie jemanden noch mehr einschüchtern, wenn Sie merkten, dass diese Person Angst vor Ihnen hatte?",
                u"5. Schlugen Sie aus Ärger so fest auf den Tisch, dass Ihnen die Faust danach weh tat?",
                u"6. Wollten Sie möglichst vor Ort sein, wenn Sie von einem grausamen Ereignis hörten?",
                u"7. Provozierten Sie andere, einfach weil es Ihnen Spaß machte?",
                u"8. Wenn Sie wütend auf jemanden waren, malten Sie sich schlimme Dinge aus, die der betreffenden Person zustoßen könnten?",
                u"9. Schauten Sie einer Schlägerei zu, auch wenn Sie sich selbst dabei in Gefahr gebracht haben?",
                u"10. Rutschte Ihnen die Hand aus, weil jemand Sie provozierte?",
                u"11. Machte es Ihnen Spaß, sich zu prügeln?",
                u"12. Wenn Sie sich bedroht fühlten, ging es Ihnen besser, wenn Sie sich vorstellten der betreffenden Person zu schaden?",
                u"13. Gewöhnten Sie sich an die Bilder von Gewalt, sodass Sie immer grausamere Bilder anschauen mussten, um genauso fasziniert zu sein?",
                u"14. Wenn Sie frustriert waren, suchten Sie körperliche Auseinandersetzungen, um den Frust abzubauen?",
                u"15. Fanden Sie Gewaltfilme aufregend, in denen die Opfer richtig leiden mussten?",
                u"16. Machte es Ihnen Spaß, mit anderen Ihre Kräfte zu messen, auch wenn Sie den anderen weh taten?",
                u"17. Fühlten Sie sich für einen Moment besser, wenn Sie Ihren Frust an anderen ausließen?",
                u"18. Stachelten Sie andere dazu an, jemanden zu beleidigen oder zu mobben?",
                u"19. Standen Sie so unter Druck, dass Sie andere Menschen beschimpften, um diesen Druck abzubauen?",
                u"20. Fühlten Sie sich stark, wenn Sie jemanden körperlich angriffen?",
                u"21. Schlugen Sie zu, wenn Sie sich in die Enge getrieben fühlten?",
                u"22. Waren Sie gemein und mussten Sie das nächste Mal gemeiner sein, um wieder die positive Aufregung zu spüren?",
                u"23. Fühlten Sie sich erleichtert, wenn Sie jemanden anschrien?",
                u"24. Faszinierte Sie eine Prügelei so sehr, dass Sie nicht aufhören konnten, sich zu prügeln?",
                u"25. Wenn Sie sich ärgerten, schlugen Sie zu, um Ihrem Ärger Luft zu machen?",
                u"26. Beschimpften oder beleidigten Sie andere, um sich gut zu fühlen?",
                u"27. Ließen Sie andere Ihren Ärger spüren, wenn Sie wegen denen nicht das bekamen, was Sie wollten?",
                u"28. Gab Ihnen eine Prügelei ein so gutes Gefühl, dass Sie auch Verletzungen in Kauf nahmen?",
                u"29. Fühlten Sie sich besser, wenn Sie jemanden schlugen, durch den Sie sich bedroht fühlten?",
                u"30. Zerstörten Sie Dinge, wenn Ihnen etwas weh tat?"
               ]

valList= range(1,len(questionList)+1)

choiceList = [
            ('0','nie'),
            ('1','selten'),
            ('2','manchmal'),
            ('3','oft'),
            ('4','sehr oft')
        ]

class Demographics(Form):

    message = TextAreaField("Vp-Nummer und Code bitte hier eingeben:" )
    submit = SubmitField("Absenden")

    qCount = 0
    frage1 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage2 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage3 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage4 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage5 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage6 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage7 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage8 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage9 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage10 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage11 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage12 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage13 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage14 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage15 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage16 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage17 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage18 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage19 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage20 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage21 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage22 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage23 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage24 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage25 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage26 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage27 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage28 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage29 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    qCount+=1
    frage30 = RadioField(questionList[qCount],
                        [validators.Required()],
                        choices=choiceList,
                        )
    submit = SubmitField("Weiter")


#############################################################################

logfile_dir = 'app/static/logfiles/'

def get_logfile():
    this_logfile= logfile_dir + 'logfile_' + str(session['userid']) + '.txt'
    return this_logfile

def make_log(logname):
    write_this = open(logname, 'w').write(
        '####### THIS IS A LOGFILE FOR THE PARAMETRIC FACE EXPERIMENT ######'+
        '\nParticipant Number: ' + str(session['userid']) +
        '\nDate and Time: '+str(datetime.datetime.now())
    )

##############
@app.route('/', methods=['GET','POST'])
@app.route('/startScreen', methods=['GET','POST'])
def startScreen():

    form = Demographics()

    if request.method == 'POST':
        session['userid'] =  request.form['message']
        #make_log(str(session['userid']))
        this_logfile = get_logfile()
        write_this = open(this_logfile, 'a').write(
        '####### THIS IS A LOGFILE FOR THE JAIL FACE EXPERIMENT ######'+
        '\n*Participant Number,' + str(session['userid']) +
        '\n*DateTime,'+str(datetime.datetime.now())
        )
        return render_template('demographics.html',form=form)
    return render_template('startScreen.html',form=form)

##############
@app.route('/demographics', methods=['GET','POST'])

def demographics():

    form = Demographics()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required')
            return render_template('demographics.html',form=form)

        this_logfile = get_logfile()
        write_this = open(this_logfile, 'a').write(
            '\nf1,'+request.form['frage1']+
            '\nf2,'+request.form['frage2']+
            '\nf3,'+request.form['frage3']+
            '\nf4,'+request.form['frage4']+
            '\nf5,'+request.form['frage5']+
            '\nf6,'+request.form['frage6']+
            '\nf7,'+request.form['frage7']+
            '\nf8,'+request.form['frage8']+
            '\nf9,'+request.form['frage9']+
            '\nf10,'+request.form['frage10']+
            '\nf11,'+request.form['frage11']+
            '\nf12,'+request.form['frage12']+
            '\nf13,'+request.form['frage13']+
            '\nf14,'+request.form['frage14']+
            '\nf15,'+request.form['frage15']+
            '\nf16,'+request.form['frage16']+
            '\nf17,'+request.form['frage17']+
            '\nf18,'+request.form['frage18']+
            '\nf19,'+request.form['frage19']+
            '\nf20,'+request.form['frage20']+
            '\nf21,'+request.form['frage21']+
            '\nf22,'+request.form['frage22']+
            '\nf23,'+request.form['frage23']+
            '\nf24,'+request.form['frage24']+
            '\nf25,'+request.form['frage25']+
            '\nf26,'+request.form['frage26']+
            '\nf27,'+request.form['frage27']+
            '\nf28,'+request.form['frage28']+
            '\nf29,'+request.form['frage29']+
            '\nf30,'+request.form['frage30']
        )
        return ('Vielen Dank!')
    return render_template('demographics.html',form=form)
