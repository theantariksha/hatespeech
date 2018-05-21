#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import subprocess
import time
class hate_speech_detection(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        

        #input
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0, columnspan=10, sticky='EW')
        self.entryVariable.set(u"Enter text here.")

        #button
        button = Tkinter.Button(self,text=u"Predict",
                                command=self.OnButtonClick)
        button.grid(column=0,row=2, padx=5, pady=10);

        #reformated
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="black",bg="white");
        label.grid(column=0,row=3,columnspan=2,sticky='W')
        self.labelVariable.set(u"Reformated")

        self.reformat_var = Tkinter.StringVar()
        label2 = Tkinter.Label(self,textvariable=self.reformat_var,
                              anchor="w",fg="red",bg="yellow");
        label2.grid(column=0,row=4,columnspan=10,sticky='W', pady=10);
        self.reformat_var.set(u"                                ");

        #sentiment score
        self.sent_variable = Tkinter.StringVar()
        label3 = Tkinter.Label(self,textvariable=self.sent_variable,
                              anchor="w",fg="black",bg="white");
        label3.grid(column=0,row=6,columnspan=2,sticky='W')
        self.sent_variable.set(u"Sentiment score")

        self.score_var = Tkinter.StringVar()
        label4 = Tkinter.Label(self,textvariable=self.score_var,
                              anchor="w",fg="red",bg="yellow");
        label4.grid(column=0,row=7,columnspan=10,sticky='W', pady=10);
        self.score_var.set(u"                                ");

        #prediction score
        self.prediction_var = Tkinter.StringVar()
        label5 = Tkinter.Label(self,textvariable=self.prediction_var,
                              anchor="w",fg="black",bg="white");
        label5.grid(column=0,row=9,columnspan=2,sticky='W')
        self.prediction_var.set(u"Prediction")

        self.predictscore_var1 = Tkinter.StringVar()
        label6 = Tkinter.Label(self,textvariable=self.predictscore_var1,
                              anchor="w",fg="red",bg="yellow");
        label6.grid(column=0,row=10,sticky='W', pady=10);
        self.predictscore_var1.set(u"                                ");
        
        self.predictscore_var2 = Tkinter.StringVar()
        label7 = Tkinter.Label(self,textvariable=self.predictscore_var2,
                              anchor="w",fg="red",bg="yellow");
        label7.grid(column=0,row=11,sticky='W');
        self.predictscore_var2.set(u"                                ");

        self.predictscore_var3 = Tkinter.StringVar()
        label8 = Tkinter.Label(self,textvariable=self.predictscore_var3,
                              anchor="w",fg="red",bg="yellow");
        label8.grid(column=0,row=12,sticky='W', pady=10);
        self.predictscore_var3.set(u"                                ");
        #answer
        self.answer_var = Tkinter.StringVar()
        label7 = Tkinter.Label(self,textvariable=self.answer_var,
                              anchor="w",fg="black",bg="white");
        label7.grid(column=0,row=13,columnspan=2,sticky='W')
        self.answer_var.set(u"Answer")

        self.ans_var = Tkinter.StringVar()
        label8 = Tkinter.Label(self,textvariable=self.ans_var,
                              anchor="w",fg="red",bg="yellow");
        label8.grid(column=0,row=14,columnspan=10,sticky='W', pady=10);
        self.ans_var.set(u"                                ");

        #clear button
        button = Tkinter.Button(self,text=u"Clear",
                                command=self.OnClear)
        button.grid(column=0,row=15, padx=5);

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry('400x400+300+200')       
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):

        input_text=self.entryVariable.get();
        file=open("user_inp.txt", "w");
        file.write(input_text.strip());
        file.close();
 
        import reformat
        subprocess.call(["python", "reformat.py"], shell=False);

        file=open("sentiment_file.txt", "r");
        line=file.readline().strip();
        self.reformat_var.set(line); 
        line=file.readline().strip();
        self.score_var.set(line); 
        file.close();

        file=open("prediction.txt", "r");
        line=file.readline().strip();
        values=line.split();
        self.predictscore_var1.set(values[0][:4]);
        self.predictscore_var2.set(values[1][:4]);
        self.predictscore_var3.set(values[2][:4]);

        line=file.readline().strip();
        answer="";
        if(line[0]=='1'):
            answer="neutral";
        elif(line[0]=='2'):
            answer="offensive";
        elif(line[0]=='3'):
            answer="hate";   

        print(answer);         
        self.ans_var.set(answer); 
        file.close();

        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnClear(self):

        self.reformat_var.set(u"                                ");
        self.score_var.set(u"                                ");
        self.predictscore_var1.set(u"                                ");
        self.predictscore_var2.set(u"                                ");
        self.predictscore_var3.set(u"                                ");

        self.ans_var.set(u"                                ");
        
if __name__ == "__main__":
    app = hate_speech_detection(None)
    app.title('Hate Speech Detection')

    app.mainloop()