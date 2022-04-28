# GDPR Fine Calculator - Group Project Legal Tech

# List of Variables

worldwide_turnover_question = "What was your enterprise's last worldwide annual turnover? "

# List of Functions

# Beginning of the program

print("What will approximately be the expected GDPR-related fine of your company in accordance with Art. 83 GDPR?")

worldwide_turnover = int(input(worldwide_turnover_question))
if worldwide_turnover <= 2000000:
    print("The enterprise falls within category A: Micro Enterprises. ")
    if worldwide_turnover <= 700000:
        basic_value = 972
        print("The enterprise falls within category A.I. Thus, the average annual turnover is determined to be"
              "350,000 €. On this basis. the basic economic value of the enterprise is 972 €.")
    elif 700001 > worldwide_turnover <= 1400000:
        basic_value = 2917
        print("The enterprise falls within category A.II. Thus the average annual turnover is determined to be"
              "1,05 Mio. €. On this basis, the basic economic value of the enterprise is 2.917 €. ")
    else:
        basic_value = 4722
        print("The enterprise falls within category A.II. Thus the average annual turnover is determined to be"
              "1.7 Mio. €. On this basis, the basic economic value of the enterprise is 4.722 €. ")

elif 2000001 > worldwide_turnover <= 10000000:
    print("The enterprise falls within category B: Small Enterprises. ")
    if 2000001 > worldwide_turnover <= 5000000:
        basic_value = 9722
        print("The enterprise falls within Category B.I. Thus, the average annual turnover is determined to be"
              "3.5 Mio. €. On this basis, the basic economic value of the enterprise is 9,722 €. ")
    elif 5000001 > worldwide_turnover <= 7500000:
        basic_value = 17361
        print("The enterprise falls within Category B.II. Thus the average annual turnover is determined to be"
              "6.25 Mio. €. On this basis, the basic economic value of the enterprise is 17,361 €.")
    else:
        basic_value = 24306
        print("The enterprise falls within Category B.III. Thus, the average annual turnover is determined to be "
              "8.75 Mio. €. On this basis, the basic economic value of the enterprise is 24,306 €. ")

elif 10000001 > worldwide_turnover <= 50000000:
    print("The enterprise falls within category C: Medium-Sized Enterprises. ")
    if 10000001 > worldwide_turnover <= 12500000:
        basic_value = 31250
        print("The enterprise falls within category C.I. Thus, the average annual turnover is determined to be"
              "11,25 Mio. €. On this basis, the basic economic value of the enterprise is 31,250 €. ")
    elif 12500001 > worldwide_turnover <= 15000000:
        basic_value = 38194
        print("The enterprise falls within category C.II. Thus, the average annual turnover is determined to be"
              "13,75 Mio. €. On this basis, the basic economic value of the enterprise is 38,194. ")
    elif 15000001 > worldwide_turnover <= 20000000:
        basic_value = 48611
        print("The enterprise falls within category C.III. Thus, the average annual turnover is determined to be"
              "17,5 Mio. €. On this basis, the basic economic value of the enterprise is 48,611 €. ")
    elif 20000001 > worldwide_turnover <= 25000000:
        basic_value = 62500
        print("The enterprise falls within category C.IV. Thus, the average annual turnover is determined to be"
              "22,5 Mio. €. On this basis, the basic economic value of the enterprise is 62,500 €. ")
    elif 25000001 > worldwide_turnover <= 30000000:
        basic_value = 76389
        print("The enterprise falls within category C.V. Thus, the average annual turnover is determined to be"
              "27,5 Mio. €. On this basis, the basic economic value of the enterprise is 76,389 €. ")
    elif 30000001 > worldwide_turnover <= 40000000:
        basic_value = 97222
        print("The enterprise falls within category C.VI. Thus, the average annual turnover is determined to be"
              "35 Mio. €. On this basis, the basic economic value of the enterprise is 97,222 €. ")
    else:
        basic_value = 125000
        print("The enterprise falls within category C.VII. Thus, the average annual turnover is determined to be"
              "45 Mio. €. On this basis, the basic economic value of the enterprise is 125,000 €. ")

else:
    print("The enterprise falls within category D: Large Enterprises. ")
    if 50000001 > worldwide_turnover <= 75000000:
        basic_value = 173611
        print("The enterprise falls within category D.I. Thus, the average annual turnover is determined to be"
              "62,5 Mio. €. On this basis, the basic economic value of the enterprise is 173,611 €. ")
    elif 75000001 > worldwide_turnover <= 100000000:
        basic_value = 243056
        print("The enterprise falls within category D.II. Thus, the average annual turnover is determined to be "
              "87,5 Mio. €. On this basis, the basic economic value of the enterprise is 243,056 €. ")
    elif 100000001 > worldwide_turnover <= 200000000:
        basic_value = 416667
        print("The enterprise falls within category D.III. Thus, the average annual turnover is determined to be"
              "150 Mio. €. On this basis, the basic economic value of the enterprise is 416,667 €. ")
    elif 200000001 > worldwide_turnover <= 300000000:
        basic_value = 694444
        print("The enterprise falls within category D.IV. Thus, the average annual turnover is determined to be"
              "250 Mio. €. On this basis, the basic economic value of the enterprise is 694,444 €. ")
    elif 300000001 > worldwide_turnover <= 400000000:
        basic_value = 972222
        print("The enterprise falls within category D.V. Thus, the average annual turnover is determined to be"
              "350 Mio. €. On this basis, the basic economic value of the enterprise is 972,222 €. ")
    elif 400000001 > worldwide_turnover <= 500000000:
        basic_value = 1250000
        print("The enterprise falls within category D.VI. Thus, the average annual turnover is determined to be"
              "450 Mio. €. On this basis, the basic economic value of the enterprise is 1,25 Mio. €. ")
    else:
        basic_value = (worldwide_turnover // 360)
        print("The basic value is:")
        print(basic_value)
        print("The enterprise falls within category D.VII. Thus, the specific annual turnover has to be used."
              "The specific annual turnover divided by 360 determines the basic economic value of the enterprise. ")


kind_of_violation = input("What kind of GDPR violation did occur? A formal violation (Art. 83 (4) GDPR) or a material "
                          "violation (Art. 83 (5) or (6) GDPR)? ")
if kind_of_violation.upper() == "FORMAL":
    severity_violation = input("How severe was the GDPR violation? (light, medium, severe, very severe) ")
    if severity_violation.upper() == "LIGHT":
        min_fine = basic_value
        max_fine = 2 * basic_value
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 1 - 2
    elif severity_violation.upper() == "MEDIUM":
        min_fine = 2 * basic_value
        max_fine = 4 * basic_value
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 2 - 4
    elif severity_violation.upper() == "SEVERE":
        min_fine = 4 * basic_value
        max_fine = 6 * basic_value
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 4 - 6
    elif severity_violation.upper() == "VERY SEVERE":
        min_fine = 6 * basic_value
        max_fine = 0.02 * worldwide_turnover
        if max_fine <= 10000000:
            max_fine = 10000000
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 6 < (max: 10 Mio. or 2% of annual turnover)
    else:
        print("Invalid input.")

elif kind_of_violation.upper() == "MATERIAL":
    severity_violation = input("How severe was the GDPR violation? (light, medium, severe, very severe) ")
    if severity_violation.upper() == "LIGHT":
        min_fine = basic_value
        max_fine = 4 * basic_value
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 1 - 4
    elif severity_violation.upper() == "MEDIUM":
        min_fine = 4 * basic_value
        max_fine = 8 * basic_value
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 4 - 8
    elif severity_violation.upper() == "SEVERE":
        min_fine = 8 * basic_value
        max_fine = 12 * basic_value
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 8 - 12
    elif severity_violation.upper() == "VERY SEVERE":
        min_fine = 12 * basic_value
        max_fine = 0.04 * worldwide_turnover
        if max_fine <= 12000000:
            max_fine == 12000000
        print("The minimum fine is:", min_fine)
        print("The maximum fine is:", max_fine)
        # Factor 12 < (max. 20 Mio. or 4% of annual turnover)
    
    else:
        print("Invalid input.")
