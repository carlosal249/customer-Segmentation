# Customer-Segmentation
<h3> Why customer Segmentation matters?</h3>

The importance of market segmentation is that it allows a business to <b>precisely</b> reach a consumer with specific needs and wants. In the long run, this <b>benefits</b> the company because they are able to use their corporate <b>resources more effectively</b> and make better strategic marketing decisions!.

the main goal of this project is to separate customers into groups, to extract insights such as: 
<ul>
<li>Do we have any standards within the customers who spend the most on the market ?</li>
<li>Do we have any group standards that could be further explored? </li>
</ul>
In this project I used a Mall database from kaggle, to create a model for customer-Segmentation, the data contains 5 variables (Gender, Id, Age, AnnualIncome, SpendingScore), where spending Score is a metric Score assigned by the mall based on customer behavior and spending nature

![Main](https://github.com/carlosal249/customer-Segmentation/blob/master/head.png)
* note: in the .ipynb file is the data exploration, and the app.py and the templates folders are for flask integration for presentation purposes

and after creating and analysing the model I found 5 Major groups:

<ul> GROUP 0:</br>   	  
 <li>:moneybag: High Income </li>
 <li>:keycap_ten: High Score </li>
 <li>:underage: 20-68 Years </li>
</ul>

<ul> GROUP 1:</br>
 <li>:moneybag: Average income </li>
 <li>:keycap_ten: Average High Score </li>
 <li>:underage: 18-70 Years </li>
</ul>

<ul> GROUP 2:</br>
 <li> :moneybag: High Income</li>
 <li> :keycap_ten: Average Low Score </li>
 <li> :underage: 18-60 Years </li>
</ul>

<ul> GROUP_3:</br>
 <li> :moneybag: Low Income </li>
 <li> :keycap_ten: High Score </li>
 <li>  :underage: 18-35 Years </li>
</ul>

<ul> GROUP 4:</br>
<li> :moneybag: Low Income </li>
<li> :keycap_ten: Average Low Score </li>
<li> :underage: 20-68 Years </li>
</ul>
  
after we separate customers into groups based on their characteristics
do we have groups who could <b>spend</b> more ? 
Yes, groups 1 and 2 could spend more 
which groups are unlikely to spend more?
probably groups 0 and 3
