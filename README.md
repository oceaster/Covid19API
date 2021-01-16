
# Covid-19 API - Challenge Summary

This is a Django Web Developer Technical Assessment for Profusion

## Instructions

In this test we will use Covid19 API https://documenter.getpostman.com/view/10808728/SzS8rjbc. Your main task will be creating a web client form and an API endpoint for travel permit inquiries using Django. Your API must consider the following conditions.

### Input data

Your API must take the following fields as input:

    1. Date of travel

    2. Date of return (optional)

    3. Country of origin

    4. Country of destination

    5. Age of traveller

### Things to be checked:

    1. Date of travel is between next 2 and 5 following working days from date of request. Otherwise, the travel permit must be denied.

    2. If Date of return is present, and date of return is within 2 months of the Date of travel, then the travel can be approved. In any other case the travel permit must be denied.

    3. Country of origin and Country of destination must be valid country names.

    4. Travel is only a llowed from countries where numberof Covid cases in Country of origin is lower than in the Country of destination.

    5. Travel is only allowed for travellers older than 21 and younger than 65. However, if traveller is older than 15 years old, he/she can travel with supervision of an adult. (You must show this prompt in your output when appropriate)
