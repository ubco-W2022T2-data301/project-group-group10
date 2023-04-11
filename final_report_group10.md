# Final Report
### Introduction

Our project set out to answer two question: 1.) What effect does smoking have on an individual's BMI as they age, and 2.) How do the medical expenses of an obese female with children, aged 20-35, differ in each region compared to a female age 36 - 50.  Our dataset compiled information on age, smoking status, number of children, BMI, and geographical regions in the United States. We felt a dataset that focused on health issues and medical expenses (especially in the US) was interesting, partly because we are residing in Canada where medical expenses are covered by the government.  We also thought the idea was interesting that smoking, which has a host of bad health effects, could actually have a positive effect (that is, keeping a person's BMI lower).

### Exploratory Data Analysis

At the outset of my EDA, I was looking at the relationships between smoking, gender, region, and BMI.  Nothing interested presented itself until I looked at the relationship between smoking and BMI and I realized that it looked like smokers did not increase their BMI as they aged, compared to non-smokers who did.

![Davidimage](images/davidimage1.jpg)

The following is my EDA that shows the relationship between BMI and medical expenses for each region. This visualization is for both males and females with all ages and all types of BMI from under weight to obesity.

![Tongimage](images/EDATong.png)

### Question 1 + Results

I began by plotting Age vs BMI for the dataset's entire population, and discovered there was a correlation between increasing age and increasing BMI.  I decided to separate out smokers from non-smokers to see what effect smoking had, and as you can see, the regression line flattens for smokers.  This suggests that smokers are less likely to gain weight as they age. Please note that for non-smokers, I used a sample to prevent overplotting.
![](images/Bmi_Age_SmokervsNon.jpg)

Next I wanted to break it down by gender. From this visualization you can see that smoking has a strong effect on a male's BMI.  The graph suggests that men who smoke do not increase their BMIs as they age, and the difference is quite apparent compared to men who do not smoke.

![](images/Bmi_Age_SmokervsNon_Men.jpg)

Finally I looked at women.  Smoking had a different effect for women than for men. From the graph below you can see that women who smoke still experienced an increase in BMI as they aged.  This is in large part due to women giving birth, and indeed my data analysis shows that more children is correlated with increased BMI.
However, the important take-away is summed up on with the boxplot on the right: this shows that the overall average BMI for women is *still lower for smokers than it is for non-smokers*. 
![](images/Bmi_Age_women.jpg)

### Question 2 + Results

**Questions: How does female in age 20-35 with obesity (bmi >30) with children in each region have different medical expenses compared to female in age 36-50 with obesity with children in each region?**

![imT0](images/VisT0.png)
According to the two bar graphs above, I have noticed that, overall, the average medical expenses seem to increase when females located in northwest, southeast, and southwest age, but there is only one region which is northeast that presents the opposite way. 

![imT2](images/VisT2.png)
To be more specific, this visualization of young females has presented BMI, so I can see that a higher BMI does not always present higher medical expenses. Besides, having a lower BMI tends to have lower medical expenses. Considering the available data, I can see that number of children between 1 and 5 is not related to how low or high of BMI is.  

![imT4](images/VisT4.png)
This visualization of middle-aged females has presented BMI as well, so I can see from available data that a higher BMI does not always present higher medical expenses for middle-aged females as I have noticed from young females' visualizations above. Besides, having a lower BMI tends to have lower medical expenses, noticing the density of lower BMI again as well. 

However, if I look at the two latest visualizations, I notice that, according to the available data, there are no high medical expenses for both young females and middle-aged females with 4 or 5 children. It is more likely that females from age 20-35 and age 36-50 would have high medical expenses with 1 or 2 children. 

### Summary/Conclusion
The key findings from our report was that individual's that smoke have a lower BMI than individuals that do not, and that a lower BMI correlates with lower medical expenses, though that can be counteracted by children and age.  We learned the answers to our research questions, which were 1.) That individual's who smoke can expect a surprising benefit from an otherwise unhealthy activity: that it helps decrease a person's BMI as they age. 2.) We learned that women with lower BMIs experience lower medical expenses, but that regardless of BMI, based on available data, having one or two children can increase medical expenses.
