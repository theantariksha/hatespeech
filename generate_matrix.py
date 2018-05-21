#seq-4
from __future__ import print_function
import time;
import sys;
import subprocess

def reset():
    
    oup=dict();
    with open("feature_removed.txt", "r") as infile:
        
        for line in infile:

            words=line.split();
            oup[words[0]]=0;
    return oup;

oup=reset();

for k in range(0, 1):

    file=open("reformated_file.txt", "r");
    senti_file=open("sentiment_file.txt", "r");
    output_file=open("matrix.txt", "w");
    
    
    #time.sleep(3);
    for line in file:
        
        for word in oup:
            oup[word]=0;
        
        words=line.split();
        for j in range(0, len(words)):
            letters=list(words[j]);
            length=len(letters);
            
            # for i in range(0, length-1):
            #   feature="".join(letters[i:i+2]);
            #   if(feature in oup):
            #       oup[feature]=1;
            # for i in range(0, length-2):
            #   feature="".join(letters[i:i+3]);
            #   if(feature in oup):
            #       oup[feature]=1;
            if length<4:
                feature="".join(letters);
                if(feature in oup):
                    oup[feature]=1;
                    continue;
            for i in range(0, length-3):
                feature="".join(letters[i:i+4]);
                if(feature in oup):
                    oup[feature]=1;
                 
        output_vect="";
        for words in oup:
            output_vect+=str(oup[words])+" ";

        senti_line=senti_file.readline();
        senti_values=senti_file.readline().strip().split(",")[:-1];  
        
        for values in senti_values:
            output_vect+=values+" ";

        output_file.write(output_vect);

    file.close();
    senti_file.close();
    output_file.close();    
import calculate
subprocess.call(["python", "calculate.py"], shell=False);