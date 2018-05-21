x_file=open("matrix.txt", "r");
line=x_file.readline();
values=line.split();
x=list();
x.append(1.0);
for value in values:
	x.append(float(value));
x_file.close();

theta1_file=open("theta1.txt", "r");
i=0;
theta1=list();
for line in theta1_file:

	i=i+1;
	if(i<6):
		continue;
	line=line.strip();
	if(len(line)==0):
		break;
	values=line.split();
	temp=list();
	for value in values:
		temp.append(float(value));
	theta1.append(temp);
theta1_file.close();

theta1_transpose=list();
for i in range(len(theta1[0])):
	temp=list();
	for j in range(len(theta1)):
		temp.append(0.0);
	theta1_transpose.append(temp);	

for i in range(len(theta1)):   
   for j in range(len(theta1[0])):
       theta1_transpose[j][i] = theta1[i][j]

# print len(theta1_transpose);


theta2_file=open("theta2.txt", "r");
i=0;
theta2=list();
for line in theta2_file:

	i=i+1;
	if(i<6):
		continue;
	line=line.strip();
	if(len(line)==0):
		break;
	values=line.split();
	temp=list();
	for value in values:
		temp.append(float(value));
	theta2.append(temp);
theta2_file.close();

theta2_transpose=list();
for i in range(len(theta2[0])):
	temp=list();
	for j in range(len(theta2)):
		temp.append(0.0);
	theta2_transpose.append(temp);	

for i in range(len(theta2)):   
   for j in range(len(theta2[0])):
       theta2_transpose[j][i] = theta2[i][j]

# print len(theta2_transpose);

hidden_layer_output=list();
temp=list();
for i in range(len(theta1)):	
	temp.append(0.0);	
hidden_layer_output.append(temp);

for i in range(1):
   for j in range(len(theta1_transpose[0])):
       for k in range(len(theta1_transpose)):
           hidden_layer_output[i][j] += x[k] * theta1_transpose[k][j];
for i in range(len(hidden_layer_output[0])):
	hidden_layer_output[0][i]=1/(1+(2.71**(-hidden_layer_output[0][i])));

hidden_layer_output[0].insert(0, 1.0);
# print len(hidden_layer_output[0]);

result=list();
temp=list();
for i in range(len(theta2)):	
	temp.append(0.0);	
result.append(temp);

for i in range(1):
   for j in range(len(theta2_transpose[0])):
       for k in range(len(theta2_transpose)):
           result[i][j] += hidden_layer_output[i][k] * theta2_transpose[k][j];
for i in range(len(result[0])):
	result[0][i]=1/(1+(2.71**(-result[0][i])));

prediction=open("prediction.txt", "w");
prediction.write(str(result[0][0])+" "+str(result[0][1])+" "+str(result[0][2]));
element, index = max(list(zip(result[0],range(len(result[0])))));
prediction.write("\n"+str(index+1));
prediction.close();