1. Run using "python main.py"

Input -

1. Enter the text to be processed in the given field
2. Click on Predict

Output -

1. Reformated - The input is processed and reformated by removing illelag characters, multiple spaces, etc.
2. Sentiment Score-
A sentiment feature vector is generated in the following way:
<original_class tweet> and the corresponding feature vector is
<avg(pos-neg), min(pos-neg), max( pos-neg), avg(positive), avg(negative), max(positive), max(negative), min(positive), min(negative), pos_score(senti_tool), neg_score(senti_tool2)>
3. Prediction gives the probability of each class corresponding to "neutral", "offensive", "hate" respectively.

Maintainers:
Souvik Mondal <mondalsouvik804@gmail.com>
Antariksha Ray <theantariksharay@gmail.com>