from __future__ import print_function
import nltk
from nltk.corpus import sentiwordnet as swn
from senti_classifier import senti_classifier
import subprocess

no_of_files=1;
for j in range(1, no_of_files+1):

    with open("reformated_file.txt", "r") as infile:

        sentinent_file=open("sentiment_file.txt", "w");
        for line in infile:

    
            sentinent_file.write(line+"\n");
            try:
                sentences = nltk.sent_tokenize(line);
                stokens = [nltk.word_tokenize(sent) for sent in sentences]
            except Exception as e:
                continue;
            taggedlist=[]
            for stoken in stokens:        
                taggedlist.append(nltk.pos_tag(stoken))
               
            wnl = nltk.WordNetLemmatizer()
            #keep average score
            score_list=[]
            #keep min score
            score_min_list=[]
            #keep max score
            score_max_list=[]
            #keep avg positive
            score_avg_positive=[];
            #keep avg negatie
            score_avg_negative=[];
            #keep max positive
            score_max_positive=[];
            #keep max negative
            score_max_negative=[];
            #keep min positive
            score_min_positive=[];
            #keep min negative
            score_min_negative=[];

            #for every line in tweet
            for idx,taggedsent in enumerate(taggedlist):
                score_list.append([])
                score_min_list.append([])
                score_max_list.append([])
                score_avg_positive.append([])
                score_avg_negative.append([])
                score_max_positive.append([])
                score_max_negative.append([])
                score_min_positive.append([])
                score_min_negative.append([])

                for idx2,t in enumerate(taggedsent):

                    score=0;
                    score_max=0;
                    score_min=1;
                    temp_avg_positive=0;
                    temp_avg_negative=0;
                    temp_max_positive=0;
                    temp_min_positive=1;
                    temp_max_negative=0;
                    temp_min_negative=1;
                    newtag=''
                    try:
                        lemmatized=wnl.lemmatize(t[0]);
                    except Exception as e:
                        continue;    
                    if t[1].startswith('NN'):
                        newtag='n'
                    elif t[1].startswith('JJ'):
                        newtag='a'
                    elif t[1].startswith('V'):
                        newtag='v'
                    elif t[1].startswith('R'):
                        newtag='r'
                    else:
                        newtag=''       
                    if(newtag!=''):    
                        synsets = list(swn.senti_synsets(lemmatized, newtag))      
                          
                        if(len(synsets)>0):
                            length=0;
                            for syn in synsets:
                                if syn.pos_score==0 and syn.neg_score==0:
                                    continue;
                                length+=1;
                                temp=syn.pos_score()-syn.neg_score();
                                score+=temp;
                                temp_avg_positive+=syn.pos_score();
                                temp_avg_negative+=syn.neg_score();
                                temp_min_positive=min(temp_min_positive, syn.pos_score());
                                temp_max_positive=max(temp_max_positive, syn.pos_score());
                                temp_min_negative=min(temp_min_negative, syn.neg_score());
                                temp_max_negative=max(temp_max_negative, syn.neg_score());
                                score_max=max(score_max, temp);
                                score_min=min(score_min, temp);
                           
                            score=score/length;
                            temp_avg_positive/=length;
                            temp_avg_negative/=length;
                            

                            score_list[idx].append(score);
                            score_min_list[idx].append(score_min);
                            score_max_list[idx].append(score_max);
                            score_avg_positive[idx].append(temp_avg_positive);
                            score_avg_negative[idx].append(temp_avg_negative);
                            score_max_positive[idx].append(temp_max_positive);
                            score_max_negative[idx].append(temp_max_negative);
                            score_min_positive[idx].append(temp_min_positive);
                            score_min_negative[idx].append(temp_min_negative);
            
            line_avg=0.0;
            i=0;



            for sentence in score_list:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");


            line_avg=0.0;
            i=0;
            for sentence in score_min_list:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;
            for sentence in score_max_list:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;
            for sentence in score_avg_positive:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;

            for sentence in score_avg_negative:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;

           
            for sentence in score_max_positive:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;
            for sentence in score_max_negative:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;
            for sentence in score_min_positive:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");

            line_avg=0.0;
            i=0;
            for sentence in score_min_negative:     
                for scores in sentence:
                    line_avg+=scores;
                    i+=1;
            if i!=0:
                line_avg=line_avg/i;
                sentinent_file.write(str(round(line_avg, 3))+", ");
            else:
                sentinent_file.write("0, ");
            try:
                pos_score, neg_score = senti_classifier.polarity_scores(sentences)
            except Exception as e:
                pos_score=neg_score=0;
            sentinent_file.write(str(pos_score)+", "+str(neg_score)+", ");

        sentinent_file.close();
        #end of loop tweets    

import generate_matrix;        
subprocess.call(["python", "generate_matrix.py"], shell=False);        