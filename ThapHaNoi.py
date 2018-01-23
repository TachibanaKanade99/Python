def ThapHaNoi(n, thap_1, thap_2, thap_3):
    if n == 1:
        print("chuyen tu", thap_1, "sang", thap_3)
    else:
        ThapHaNoi(n-1, thap_1, thap_3, thap_2)
        print("chuyen tu", thap_1,"sang", thap_3)
        ThapHaNoi(n-1, thap_2, thap_1, thap_3)

ThapHaNoi(5, 1, 2, 3)
