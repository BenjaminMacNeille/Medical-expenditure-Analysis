# Medical-expenditure-Analysis
This repository holds an analysis of medical expenditures using the Medical Expenditure Panel Survey. The Medical Expenditure Panel Survey is a dataset released annually and comprised of several components that describe different types of medical events and population characteristics.

I used Emergency Room, Household, Inpatient, Office-Based, Outpatient, and Prescription event components in conjunction with Conditions and Population Characteristics components to predict expenditures for respondents with mood disorders.

I decided to analyze respondents with mood disorders because there comprised a relatively large group among the 760 classifications included in the dataset, and because this group of individuals have been and continue to be affected by shifting medical policy (https://www.forbes.com/sites/brucejapsen/2017/01/13/psychologists-to-trump-coverage-must-include-mental-health-benefits/#26f3ba166a0c).

My general hypothesis entering this project was that mood disorders are likely under-diagnosed, and thus may be the cause of costly and severe (high SOI, i.e. severity of illness) medical events when early identification and intervention was not implemented.

The primary research question became: Which medical events are both costly and severe for respondents with mood disorders? I filtered event types to those designated with the mood disorder classification and combined each component's expenditures along with population characteristics. I used a GLM and found that inpatient visits, while relatively rare for those with mood disorders, were a major source of expenditures.

Inpatient events are also considered very severe, so predicting the types of care that may prevent inpatient events are a source of interest to researchers. The current goal of this project is to identify the features that indicate whether a respondent will have an inpatient event.

Within this repository is source code in the form of a Jupyter Notebook (/src), literature review and data understanding (/notes), and a presentation of preliminary findings.
