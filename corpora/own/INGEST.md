# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 312 (the final check needs at least 200)
- Words: 489,276
- Estimated tokens (words times 1.4): 684,986 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 0

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `application-and-verification-guide_ch1-application-process-fafsa__p001-005` | 1,858 | 2386 | - | - |
| `application-and-verification-guide_ch1-application-process-fafsa__p006-009` | 1,170 | 1889 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p001-005` | 1,650 | 2044 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p006-010` | 1,928 | 2344 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p011-015` | 2,400 | 2792 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p016-020` | 1,609 | 2003 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p021-025` | 1,841 | 2246 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p026-030` | 2,744 | 3267 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p031-035` | 2,030 | 2464 | - | - |
| `application-and-verification-guide_ch2-filling-out-fafsa-form__p036-041` | 2,088 | 2104 | - | - |
| `application-and-verification-guide_ch3-student-aid-index-sai-and__p001-005` | 1,094 | 1269 | - | - |
| `application-and-verification-guide_ch3-student-aid-index-sai-and__p006-010` | 1,437 | 1887 | - | - |
| `application-and-verification-guide_ch3-student-aid-index-sai-and__p011-015` | 1,287 | 1742 | - | - |
| `application-and-verification-guide_ch3-student-aid-index-sai-and__p016-017` | 545 | 1782 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p001-005` | 1,039 | 1364 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p006-010` | 1,683 | 2135 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p011-015` | 1,762 | 2102 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p016-020` | 2,276 | 2738 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p021-025` | 1,844 | 2249 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p026-030` | 2,149 | 2691 | - | - |
| `application-and-verification-guide_ch4-verification-updates-and__p031-033` | 838 | 1795 | - | - |
| `application-and-verification-guide_ch5-special-cases__p001-005` | 1,901 | 2441 | - | - |
| `application-and-verification-guide_ch5-special-cases__p006-010` | 1,593 | 2026 | - | - |
| `application-and-verification-guide_ch5-special-cases__p011-015` | 1,755 | 2289 | - | - |
| `application-and-verification-guide_ch5-special-cases__p016-018` | 757 | 1642 | - | - |
| `vol1_ch1-school-determined-requirements__p001-005` | 2,236 | 2778 | - | - |
| `vol1_ch1-school-determined-requirements__p006-010` | 1,732 | 2203 | - | - |
| `vol1_ch1-school-determined-requirements__p011-015` | 1,689 | 2187 | - | - |
| `vol1_ch1-school-determined-requirements__p016-020` | 1,903 | 2406 | - | - |
| `vol1_ch1-school-determined-requirements__p021-025` | 2,585 | 3100 | - | - |
| `vol1_ch1-school-determined-requirements__p026-030` | 2,079 | 2562 | - | - |
| `vol1_ch1-school-determined-requirements__p031-035` | 2,165 | 2689 | - | - |
| `vol1_ch1-school-determined-requirements__p036-039` | 1,551 | 2499 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p001-005` | 1,986 | 2523 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p006-010` | 1,923 | 2401 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p011-015` | 1,865 | 2407 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p016-020` | 2,676 | 3335 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p021-025` | 2,228 | 2834 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p026-030` | 2,501 | 3240 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p031-035` | 1,438 | 1934 | - | - |
| `vol1_ch2-us-citizenship-eligible-noncitizens__p036-037` | 628 | 2074 | - | - |
| `vol1_ch3-nslds-financial-aid-history__p001-005` | 1,811 | 2219 | - | - |
| `vol1_ch3-nslds-financial-aid-history__p006-010` | 2,614 | 3215 | - | - |
| `vol1_ch3-nslds-financial-aid-history__p011-015` | 1,927 | 2408 | - | - |
| `vol1_ch3-nslds-financial-aid-history__p016-019` | 1,379 | 2162 | - | - |
| `vol1_ch4-social-security-number` | 2,327 | 2758 | - | - |
| `vol2_ch1-institutional-eligibility__p001-005` | 920 | 1224 | - | - |
| `vol2_ch1-institutional-eligibility__p006-010` | 1,848 | 2437 | - | - |
| `vol2_ch1-institutional-eligibility__p011-015` | 1,299 | 1656 | - | - |
| `vol2_ch1-institutional-eligibility__p016-020` | 1,695 | 2152 | - | - |
| `vol2_ch1-institutional-eligibility__p021-025` | 1,401 | 1806 | - | - |
| `vol2_ch1-institutional-eligibility__p026-029` | 798 | 1326 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p001-005` | 1,974 | 2509 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p006-010` | 1,360 | 1809 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p011-015` | 1,877 | 2523 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p016-020` | 1,929 | 2530 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p021-025` | 2,018 | 2602 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p026-030` | 1,588 | 2152 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p031-035` | 1,545 | 2077 | - | - |
| `vol2_ch2-program-eligibility-written-arrangements-and-distance-e__p036-041` | 1,970 | 2014 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p001-005` | 1,047 | 1419 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p006-010` | 1,822 | 2357 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p011-015` | 1,633 | 2126 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p016-020` | 1,300 | 1766 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p021-025` | 1,558 | 2095 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p026-030` | 1,964 | 2608 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p031-035` | 1,672 | 2123 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p036-040` | 1,667 | 2099 | - | - |
| `vol2_ch3-title-iv-administrative-and-related-requirements__p041-045` | 1,655 | 2082 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p001-005` | 1,809 | 2306 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p006-010` | 2,015 | 2513 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p011-015` | 2,281 | 2960 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p016-020` | 1,446 | 1943 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p021-025` | 1,273 | 1771 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p026-030` | 1,251 | 1543 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p031-035` | 1,536 | 1903 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p036-040` | 1,627 | 2050 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p041-045` | 1,646 | 2083 | - | - |
| `vol2_ch4-audits-standards-limitations-cohort-default-rates__p046-048` | 764 | 1591 | - | - |
| `vol2_ch5-updating-application-information__p001-005` | 1,163 | 1514 | - | - |
| `vol2_ch5-updating-application-information__p006-010` | 1,552 | 1902 | - | - |
| `vol2_ch5-updating-application-information__p011-015` | 1,923 | 2445 | - | - |
| `vol2_ch5-updating-application-information__p016-020` | 1,488 | 1896 | - | - |
| `vol2_ch5-updating-application-information__p021-025` | 1,805 | 2243 | - | - |
| `vol2_ch5-updating-application-information__p026-030` | 1,867 | 2463 | - | - |
| `vol2_ch5-updating-application-information__p031-036` | 1,285 | 1333 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p001-005` | 1,157 | 1532 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p006-010` | 1,423 | 1885 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p016-020` | 1,265 | 1705 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p021-025` | 1,521 | 1954 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p026-030` | 1,495 | 2046 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p031-035` | 1,342 | 1754 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p036-040` | 1,394 | 1813 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p041-045` | 1,540 | 2056 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p046-050` | 1,381 | 1708 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p051-055` | 1,334 | 1804 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p056-060` | 1,220 | 1555 | - | - |
| `vol2_ch6-consumer-information-and-school-reporting__p061-065` | 1,113 | 1482 | - | - |
| `vol2_ch7-record-keeping-privacy-electronic-processes__p001-005` | 1,148 | 1506 | - | - |
| `vol2_ch7-record-keeping-privacy-electronic-processes__p006-010` | 1,196 | 1518 | - | - |
| `vol2_ch7-record-keeping-privacy-electronic-processes__p011-015` | 1,925 | 2447 | - | - |
| `vol2_ch7-record-keeping-privacy-electronic-processes__p016-020` | 1,911 | 2487 | - | - |
| `vol2_ch7-record-keeping-privacy-electronic-processes__p021-025` | 1,447 | 2022 | - | - |
| `vol2_ch8-program-reviews-sanctions-closeout__p001-005` | 1,279 | 1712 | - | - |
| `vol2_ch8-program-reviews-sanctions-closeout__p006-010` | 1,338 | 1760 | - | - |
| `vol2_ch8-program-reviews-sanctions-closeout__p011-015` | 1,507 | 1891 | - | - |
| `vol2_ch8-program-reviews-sanctions-closeout__p016-020` | 1,406 | 1784 | - | - |
| `vol3_ch1-academic-years-academic-calendars-payment-periods-and-d__p001-005` | 2,946 | 3601 | - | - |
| `vol3_ch1-academic-years-academic-calendars-payment-periods-and-d__p006-010` | 2,330 | 2883 | - | - |
| `vol3_ch1-academic-years-academic-calendars-payment-periods-and-d__p011-015` | 1,838 | 2199 | - | - |
| `vol3_ch1-academic-years-academic-calendars-payment-periods-and-d__p016-020` | 2,559 | 3111 | - | - |
| `vol3_ch1-academic-years-academic-calendars-payment-periods-and-d__p021-025` | 2,238 | 2804 | - | - |
| `vol3_ch1-academic-years-academic-calendars-payment-periods-and-d__p026-029` | 891 | 1364 | - | - |
| `vol3_ch2-cost-attendance-budget__p001-005` | 2,138 | 2614 | - | - |
| `vol3_ch2-cost-attendance-budget__p006-010` | 1,879 | 2318 | - | - |
| `vol3_ch2-cost-attendance-budget__p011-014` | 1,809 | 2662 | - | - |
| `vol3_ch3-packaging-aid__p001-005` | 2,145 | 2609 | - | - |
| `vol3_ch3-packaging-aid__p006-010` | 1,596 | 1972 | - | - |
| `vol3_ch3-packaging-aid__p011-015` | 1,898 | 2368 | - | - |
| `vol3_ch3-packaging-aid__p016-020` | 1,646 | 2049 | - | - |
| `vol3_ch3-packaging-aid__p021-025` | 1,593 | 2051 | - | - |
| `vol4_appx-accounting-systems__p001-005` | 1,604 | 2119 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p006-010` | 949 | 1275 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p011-015` | 680 | 854 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p016-020` | 904 | 1121 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p021-025` | 795 | 997 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p026-030` | 1,000 | 1266 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p031-035` | 1,057 | 1340 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p036-040` | 906 | 1067 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p041-045` | 999 | 1134 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p046-050` | 1,065 | 1229 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p051-055` | 948 | 1034 | - | 2 running line(s) removed |
| `vol4_appx-accounting-systems__p056-059` | 524 | 821 | - | 2 running line(s) removed |
| `vol4_appx-b-schools-financial-management-systems__p001-005` | 1,071 | 1508 | - | - |
| `vol4_appx-b-schools-financial-management-systems__p006-010` | 914 | 1248 | - | - |
| `vol4_appx-b-schools-financial-management-systems__p011-015` | 1,090 | 1464 | - | - |
| `vol4_appx-b-schools-financial-management-systems__p016-020` | 1,820 | 2428 | - | - |
| `vol4_appx-b-schools-financial-management-systems__p021-025` | 1,413 | 1816 | - | - |
| `vol4_appx-b-schools-financial-management-systems__p026-031` | 1,344 | 1514 | - | - |
| `vol4_ch1-requesting-and-managing-title-iv-funds__p001-005` | 1,079 | 1398 | - | - |
| `vol4_ch1-requesting-and-managing-title-iv-funds__p006-010` | 1,424 | 1758 | - | - |
| `vol4_ch1-requesting-and-managing-title-iv-funds__p011-015` | 1,100 | 1404 | - | - |
| `vol4_ch1-requesting-and-managing-title-iv-funds__p016-020` | 1,804 | 2338 | - | - |
| `vol4_ch1-requesting-and-managing-title-iv-funds__p021-025` | 1,582 | 1945 | - | - |
| `vol4_ch1-requesting-and-managing-title-iv-funds__p026-029` | 907 | 1366 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p001-005` | 1,745 | 2101 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p006-010` | 1,644 | 2037 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p011-015` | 1,089 | 1329 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p016-020` | 1,530 | 1901 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p021-025` | 1,760 | 2121 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p026-030` | 1,686 | 2104 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p031-035` | 1,284 | 1572 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p036-040` | 1,681 | 1965 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p041-045` | 2,304 | 2702 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p046-050` | 1,562 | 1912 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p051-055` | 1,526 | 1971 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p056-060` | 1,449 | 1812 | - | - |
| `vol4_ch2-disbursing-title-iv-funds__p061-064` | 1,238 | 1991 | - | - |
| `vol4_ch3-overawards-and-overpayments__p001-005` | 1,797 | 2192 | - | - |
| `vol4_ch3-overawards-and-overpayments__p006-010` | 1,953 | 2433 | - | - |
| `vol4_ch3-overawards-and-overpayments__p011-015` | 2,084 | 2539 | - | - |
| `vol4_ch3-overawards-and-overpayments__p016-019` | 826 | 1298 | - | - |
| `vol4_ch4-returning-title-iv-funds__p001-005` | 1,534 | 1878 | - | - |
| `vol4_ch4-returning-title-iv-funds__p006-010` | 1,248 | 1505 | - | - |
| `vol4_ch4-returning-title-iv-funds__p011-013` | 945 | 1893 | - | - |
| `vol4_ch5-reconciliation-pell-grant-and-campus-based-programs__p001-005` | 1,539 | 2054 | - | - |
| `vol4_ch5-reconciliation-pell-grant-and-campus-based-programs__p006-010` | 1,725 | 2294 | - | - |
| `vol4_ch5-reconciliation-pell-grant-and-campus-based-programs__p011-016` | 2,105 | 2238 | - | - |
| `vol4_ch6-reconciliation-direct-loan-program__p001-005` | 1,750 | 2219 | - | - |
| `vol4_ch6-reconciliation-direct-loan-program__p006-010` | 1,506 | 1885 | - | - |
| `vol4_ch6-reconciliation-direct-loan-program__p011-015` | 1,532 | 1866 | - | - |
| `vol4_ch6-reconciliation-direct-loan-program__p016-020` | 1,258 | 1627 | - | - |
| `vol4_ch6-reconciliation-direct-loan-program__p021-025` | 1,435 | 1808 | - | - |
| `vol4_ch6-reconciliation-direct-loan-program__p026-029` | 505 | 854 | - | - |
| `vol5_appx-appendix-return-title-iv-aid-worksheets` | 223 | 719 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p001-005` | 1,932 | 2366 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p006-010` | 2,494 | 3092 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p011-015` | 2,155 | 2711 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p016-020` | 2,055 | 2512 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p021-025` | 2,401 | 2835 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p026-030` | 2,074 | 2603 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p031-035` | 1,979 | 2399 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p036-040` | 1,975 | 2416 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p041-045` | 1,990 | 2407 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p046-050` | 1,461 | 1755 | - | - |
| `vol5_ch1-general-requirements-withdrawals-and-return-title-iv-fu__p051-053` | 841 | 1637 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p001-005` | 2,268 | 2782 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p006-010` | 2,240 | 2759 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p011-015` | 2,143 | 2680 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p016-020` | 2,556 | 3154 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p021-025` | 1,707 | 2176 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p026-030` | 2,267 | 2719 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p031-035` | 1,808 | 2081 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p036-040` | 1,886 | 2242 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p041-045` | 2,439 | 2931 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p046-050` | 2,857 | 3351 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-1__p051-052` | 477 | 1404 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p001-005` | 2,137 | 2555 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p006-010` | 1,790 | 2188 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p011-015` | 1,736 | 2057 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p016-020` | 1,784 | 2134 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p021-025` | 2,159 | 2722 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p026-030` | 1,703 | 2068 | - | - |
| `vol5_ch2-steps-return-title-iv-aid-calculation-part-2__p031-034` | 998 | 1628 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p001-005` | 562 | 710 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p006-010` | 915 | 1078 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p011-015` | 1,038 | 1221 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p016-020` | 760 | 831 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p021-025` | 824 | 984 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p026-030` | 812 | 914 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p031-035` | 766 | 874 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p036-040` | 784 | 897 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p041-045` | 693 | 830 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p046-050` | 1,199 | 1371 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-1__p051-054` | 516 | 692 | - | 1 running line(s) removed |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p001-005` | 540 | 669 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p006-010` | 1,178 | 1358 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p011-015` | 807 | 916 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p016-020` | 1,087 | 1331 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p021-025` | 1,135 | 1277 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p026-030` | 902 | 1137 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p031-035` | 666 | 740 | - | - |
| `vol5_ch3-return-title-iv-r2t4-funds-case-studies-part-2__p036-038` | 323 | 594 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p001-005` | 1,487 | 1952 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p006-010` | 1,434 | 1887 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p011-015` | 1,964 | 2488 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p016-020` | 1,661 | 1981 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p021-025` | 1,798 | 2228 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p026-030` | 1,671 | 2050 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p031-035` | 1,391 | 1779 | - | - |
| `vol6_ch1-campus-based-programs-common-elements__p036-040` | 1,158 | 1400 | - | - |
| `vol6_ch2-federal-work-study-program__p001-005` | 2,037 | 2490 | - | - |
| `vol6_ch2-federal-work-study-program__p006-010` | 1,719 | 2086 | - | - |
| `vol6_ch2-federal-work-study-program__p011-015` | 1,594 | 1969 | - | - |
| `vol6_ch2-federal-work-study-program__p016-020` | 1,446 | 1823 | - | - |
| `vol6_ch2-federal-work-study-program__p021-025` | 1,544 | 1890 | - | - |
| `vol6_ch2-federal-work-study-program__p026-030` | 1,521 | 2002 | - | - |
| `vol6_ch2-federal-work-study-program__p031-035` | 1,349 | 1838 | - | - |
| `vol6_ch2-federal-work-study-program__p036-040` | 1,732 | 2166 | - | - |
| `vol6_ch2-federal-work-study-program__p041-045` | 1,986 | 2569 | - | - |
| `vol6_ch2-federal-work-study-program__p046-050` | 1,462 | 1811 | - | - |
| `vol6_ch2-federal-work-study-program__p051-055` | 1,116 | 1495 | - | - |
| `vol6_ch2-federal-work-study-program__p056-057` | 432 | 1384 | - | - |
| `vol6_ch3-participating-perkins-loan-program__p001-005` | 1,914 | 2421 | - | - |
| `vol6_ch3-participating-perkins-loan-program__p006-010` | 1,908 | 2479 | - | - |
| `vol6_ch3-participating-perkins-loan-program__p011-015` | 1,294 | 1670 | - | - |
| `vol6_ch3-participating-perkins-loan-program__p016-020` | 922 | 1194 | - | - |
| `vol6_ch3-participating-perkins-loan-program__p021-025` | 1,945 | 2539 | - | - |
| `vol6_ch3-participating-perkins-loan-program__p026-028` | 949 | 1993 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p001-005` | 1,858 | 2243 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p006-010` | 1,492 | 1842 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p011-015` | 1,539 | 1921 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p016-020` | 1,791 | 2305 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p021-025` | 1,713 | 2182 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p026-030` | 1,190 | 1563 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p031-035` | 1,381 | 1810 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p036-040` | 1,701 | 2203 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p041-045` | 1,482 | 1993 | - | - |
| `vol6_ch4-perkins-repayment-plans-forbearance-deferment-discharge__p046-051` | 2,587 | 2662 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p001-005` | 1,391 | 1727 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p006-010` | 1,442 | 1808 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p011-015` | 1,622 | 2033 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p016-020` | 1,933 | 2386 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p021-025` | 1,648 | 2068 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p026-030` | 1,334 | 1696 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p031-035` | 1,384 | 1759 | - | - |
| `vol6_ch5-perkins-loan-billing-collection-and-default__p036-038` | 470 | 1118 | - | - |
| `vol6_ch6-federal-supplemental-educational-opportunity-grant-prog` | 1,686 | 2539 | - | - |
| `vol7_appx-pell-formula-summaries__p001-005` | 1,105 | 1402 | - | 1 running line(s) removed |
| `vol7_appx-pell-formula-summaries__p006-007` | 450 | 1367 | - | 1 running line(s) removed |
| `vol7_ch1-student-eligibility-pell-grants__p001-005` | 1,810 | 2320 | - | - |
| `vol7_ch1-student-eligibility-pell-grants__p006-008` | 871 | 1821 | - | - |
| `vol7_ch2-calculating-pell-grants__p001-005` | 1,450 | 1695 | - | 1 running line(s) removed |
| `vol7_ch2-calculating-pell-grants__p006-008` | 1,006 | 2022 | - | 1 running line(s) removed |
| `vol7_ch3-pell-grant-enrollment-intensity-and-cost-attendance__p001-005` | 1,696 | 2098 | - | - |
| `vol7_ch3-pell-grant-enrollment-intensity-and-cost-attendance__p006-009` | 1,697 | 2527 | - | - |
| `vol7_ch4-calculating-annual-awards-using-pell-grant-formulas__p001-005` | 1,304 | 1569 | - | - |
| `vol7_ch4-calculating-annual-awards-using-pell-grant-formulas__p006-010` | 1,355 | 1610 | - | - |
| `vol7_ch4-calculating-annual-awards-using-pell-grant-formulas__p011-015` | 1,503 | 1765 | - | - |
| `vol7_ch4-calculating-annual-awards-using-pell-grant-formulas__p016-021` | 1,900 | 1947 | - | - |
| `vol7_ch5-summer-terms-crossover-payment-periods-and-year-round-p__p001-005` | 2,354 | 2737 | - | - |
| `vol7_ch5-summer-terms-crossover-payment-periods-and-year-round-p__p006-007` | 986 | 2952 | - | - |
| `vol7_ch6-transfer-students-and-remaining-eligibility__p001-005` | 2,210 | 2706 | - | - |
| `vol7_ch6-transfer-students-and-remaining-eligibility__p006-007` | 510 | 1624 | - | - |
| `vol7_ch7-initial-calculations-recalculations-and-overawards__p001-005` | 2,387 | 2930 | - | - |
| `vol7_ch7-initial-calculations-recalculations-and-overawards__p006-009` | 1,641 | 2492 | - | - |
| `vol7_ch8-pell-grant-lifetime-eligibility-used-leu__p001-005` | 1,671 | 2035 | - | - |
| `vol7_ch8-pell-grant-lifetime-eligibility-used-leu__p006-007` | 348 | 1102 | - | - |
| `vol8_ch1-student-and-parent-eligibility-direct-loans__p001-005` | 1,911 | 2375 | - | - |
| `vol8_ch1-student-and-parent-eligibility-direct-loans__p006-010` | 1,817 | 2223 | - | - |
| `vol8_ch1-student-and-parent-eligibility-direct-loans__p011-016` | 2,006 | 2126 | - | - |
| `vol8_ch2-direct-loan-counseling__p001-005` | 1,606 | 2107 | - | - |
| `vol8_ch2-direct-loan-counseling__p006-010` | 1,516 | 2024 | - | - |
| `vol8_ch3-direct-loan-origination-loan-periods-and-disbursements__p001-005` | 1,863 | 2259 | - | - |
| `vol8_ch3-direct-loan-origination-loan-periods-and-disbursements__p006-010` | 2,474 | 2987 | - | - |
| `vol8_ch3-direct-loan-origination-loan-periods-and-disbursements__p011-015` | 2,102 | 2527 | - | - |
| `vol8_ch4-annual-and-aggregate-loan-limits__p001-005` | 1,750 | 2290 | - | - |
| `vol8_ch4-annual-and-aggregate-loan-limits__p006-010` | 2,229 | 2865 | - | - |
| `vol8_ch4-annual-and-aggregate-loan-limits__p011-015` | 1,504 | 2088 | - | - |
| `vol8_ch4-annual-and-aggregate-loan-limits__p016-018` | 1,501 | 3338 | - | - |
| `vol8_ch5-loan-limit-proration__p001-005` | 2,071 | 2489 | - | - |
| `vol8_ch5-loan-limit-proration__p006-010` | 2,243 | 2687 | - | - |
| `vol8_ch5-loan-limit-proration__p011-013` | 926 | 2036 | - | - |
| `vol8_ch6-monitoring-annual-loan-limit-progression__p001-005` | 2,434 | 2739 | - | - |
| `vol8_ch6-monitoring-annual-loan-limit-progression__p006-010` | 1,956 | 2289 | - | - |
| `vol8_ch6-monitoring-annual-loan-limit-progression__p011-015` | 1,838 | 2244 | - | - |
| `vol8_ch7-annual-loan-limits-students-who-transfer-or-change-prog__p001-005` | 2,333 | 2744 | - | - |
| `vol8_ch7-annual-loan-limits-students-who-transfer-or-change-prog__p006-007` | 906 | 2644 | - | - |
| `vol9_ch1-eligibility-teach-grants__p001-005` | 1,514 | 1930 | - | - |
| `vol9_ch1-eligibility-teach-grants__p006-007` | 338 | 1078 | - | - |
| `vol9_ch2-teach-grant-counseling-and-agreement-serve-or-repay` | 1,144 | 1875 | - | - |
| `vol9_ch3-calculating-teach-grants` | 1,916 | 2388 | - | - |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
