<h1 align=center> Customer-Segmentation </h1>
<h3> Why customer Segmentation matters?</h3>

The importance of market segmentation is that it allows a business to <b>precisely</b> reach a consumer with specific needs and wants. In the long run, this <b>benefits</b> the company because they are able to use their corporate <b>resources more effectively</b> and make better strategic marketing decisions!.

the main goal of this project is to separate customers into groups, to extract insights such as: 
<ul>
<li>Do we have any standards within the customers who spend the most on the market ?</li>
<li>Do we have any group standards that could be further explored? </li>
</ul>
In this project I used a Mall database from kaggle, to create a model for customer-Segmentation, the data contains 5 variables (Gender, Id, Age, AnnualIncome, SpendingScore), where spending Score is a metric Score assigned by the mall based on customer behavior and spending nature

![Main](https://github.com/carlosal249/customer-Segmentation/blob/master/head.png)
* note: in the Customer Segmentation.ipynb file is the data exploration and the model, the app.py and the templates folders are for flask(api) integration for presentation an deploy purposes

<h3> After creating and analysing the model I found 5 Major groups:</h3>

|Group|Income|Score|Age|
| -------- | -------- | -------- |-------- |
|GROUP 0|High Income|High score|20-68|
|GROUP 1|Average income|Average High Score|18-70|
|GROUP 2|High Income|Average Low Score|18-60|
|GROUP 3|Low Income|High score|18-35|
|GROUP 4|Low Income|Average Low Score|20-68|

<h3 align=center> Conclusion: </h3>
<p>After we separate customers into groups based on their characteristics</p>

<p> do we have groups who could <b>spend</b> more ? </br>
Yes, groups 1 and 2 could spend more</p>
<p> Do we have any standards within the customers who spend the most on the market ? </br>
 Yes we managed to separate customers by standards!</p>
<p> which groups are unlikely to spend more?</br>
 Probably groups 0 and 3</p>
