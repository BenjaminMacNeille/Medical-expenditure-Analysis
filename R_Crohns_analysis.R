library("dplyr")
conditions = read.csv("2012 - conditions.csv")
str(conditions)

crohn_marker <- conditions %>%
  mutate(crohnsICD = ifelse(ICD9CODX == "555", 1, 0)) %>%
  group_by(DUPERSID) %>%
  summarise(crohns = max(crohnsICD)) %>%
  arrange(crohns) 

population = read.csv("2012 - popchar.csv")

#bind crohn_marker with popchars by DUPERSID

popchar_crohn = left_join(population, crohn_marker, by = "DUPERSID")

View(popchar_crohn)
glimpse(popchar_crohn)
View(popchar_crohn$crohns)


#count(popchar_crohn, is.na(crohns))
#View(crohn_marker)
  
popchar_crohn$crohns[is.na(popchar_crohn$crohns)] = -1
glimpse(popchar_crohn)
head(popchar_crohn$DUPERSID)

final_df = select(popchar_crohn, SEX, AGE12X, DUPERSID, crohns, 
                  VARPSU, VARSTR, RACEV1X, MARRY12X, 
                  EDRECODE,REGION12, MSA12)
glimpse(final_df)

#make list of unique DUOERSIDS in Crohns

crohns_final = mutate(conditions, crohns = ifelse(ICD9CODX == "555", 1, 0))
crohns_filtered = select(crohns_final, DUPERSID, crohns)
View(crohns_filtered)


View(crohns_final)
summarise(crohns_final)

#add column to popchar file

population = read.csv("2012 - popchar.csv")



#unique_crohns = group_by(crohns, DUPERSID)
#View(unique_crohns)


#filter from control file any DUPERS found in Crohn's file