from nltk.stem.porter import *

import subprocess

h=open("s.txt", "w");
h.write("l");
h.close();
chars=[];
fchars=open("chars.txt", "r");
data_file="user_inp.txt";

for line in fchars:
    chars.extend(line.split());
fchars.close();
chars.append(' ');

file_list=open("reformated_file.txt", "w");

stemmer = PorterStemmer();
exception_list=[',','.','\'','\"',':', ';','?'];
with open(data_file) as infile:

    
   
    for line in infile:

        i=0;
        try:
            line=line.decode('ascii').strip();
        except Exception as e:
            line="";
        original_line=line.strip();    
        words=line.split();
        line="";
        
        for word in words:
            if(word.startswith("http")):
                word="";
            if(word.startswith("@")):
                word="";
                
            word=stemmer.stem(word);
            line=line+word+" ";

        list_line=list(line.lower());
        
        for c in list_line[0:]:
       
            if c not in chars:
                if c in exception_list:
                    list_line[i]=' ';
                else:
                    list_line[i]='*';    
            
            i+=1;

       
        num_flag=0;
        flag=0;
        lists=list();

        for c in list_line[0:]:
            if c=='*':
                flag=1;
            elif c.isdigit():
                num_flag=1;
            else:
                if flag==1:
                    lists.append('*');
                    flag=0;
                if num_flag==1:
                    lists.append(' NUM ');
                    num_flag=0;        
                lists.append(c);

        list_line=lists;                    
        if(len(list_line)!=0) :  
         
            save_line="".join(list_line);   
            
            file_list.write(save_line);     

file_list.close();

import sentiment_tag
subprocess.call(["python", "sentiment_tag.py"], shell=False);